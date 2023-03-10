from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _rec_name = "name"

    name = fields.Char(string='Name', tracking=True, translate=True)
    date_of_birth = fields.Date(string='Date of Birth')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age', inverse="_inverse_compute_age", search="_search_age",
                         tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True,
                              default='female')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many('patient.tag', string='Tag')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string="Marital Status",
                                      tracking=True)
    partner_name = fields.Char(string="Partner Name")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not acceptable !"))

    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You cannot delete a patient with appointments !"))

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)
    
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - ((today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0

    @api.depends('age')
    def _inverse_compute_age(self):
        for rec in self:
            today = date.today()
            if rec.age:
                rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_of_date = date_of_birth - relativedelta.relativedelta(years=1)
        return [('date_of_birth', '>', start_of_date), ('date_of_birth', '<=', date_of_birth)]

    def name_get(self):
        return [(record.id, '[%s] %s' % (record.ref, record.name)) for record in self]

    def action_test(self):
        print("Clicked")
        return
