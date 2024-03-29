import random
import mysql.connector

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError



class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "name"
    _order = "id desc"

    name = fields.Char(string='Sequence', default='New')
    patient_id = fields.Many2one('hospital.patient', string='Patient', ondelete='cascade')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help="Reference of the patient from patient record")
    prescription = fields.Html(string='Prescription', translate=True)
    priority = fields.Selection([
        ('0', 'Very Low'),
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High')], string='Priority')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='Status', required=True, tracking=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmasy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    operation_id = fields.Many2one('hospital.operation', string='Operation')
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    duration = fields.Float(string="Duration")
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals)

    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError(_("You can delete appointment only in draft status !"))
        return super(HospitalAppointment, self).unlink()

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("I clic to Button!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click SuccessFull',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == "draft":
                progress = random.randrange(0, 25)
            elif rec.state == "in_consultation":
                progress = random.randrange(25, 99)
            elif rec.state == "done":
                progress = 100
            else:
                progress = 0
            rec.progress = progress

    def get_mysql_data(self):
        # Конфігурація з'єднання з базою даних MySQL
        config = {
            'user': 'kaliuta_borove',
            'password': 'majwbmw',
            'host': 's64.nska.net',
            'database': 'kaliuta_borove',
        }

        # Встановлення з'єднання з базою даних
        try:
            connection = mysql.connector.connect(**config)
            if connection.is_connected():
                print('Connected to MySQL database')

                # Створення курсора
                cursor = connection.cursor()

                # Виконання запиту до бази даних
                query = "SELECT * FROM product WHERE id = 1;"
                cursor.execute(query)

                # Отримання результатів запиту
                result = cursor.fetchone()

                print(result)
                # Перевірка наявності результатів
                # if result:
                #     price_data = result[0]

                #     # Розпарсювання JSON-даних
                #     parsed_data = json.loads(price_data)
                #
                #     # Додайте решту коду для роботи з розпарсованими даними
                #     print(parsed_data)
                # else:
                #     print('No data found in the table')

                # Закриття курсора і з'єднання
                cursor.close()

        except mysql.connector.Error as e:
            print(f'Error connecting to MySQL database: {e}')
        finally:
            if connection.is_connected():
                connection.close()
                print('MySQL database connection closed')

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click SuccessFull',
                'type': 'rainbow_man',
            }
        }

class AppointmentPharmasyLines(models.Model):
    _name = "appointment.pharmasy.lines"
    _description = "Appointment Pharmasy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer('Quantity', default=1)
    appointment_id = fields.Many2one('hospital.appointment', 'Appointment')
