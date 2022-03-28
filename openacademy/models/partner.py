from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string="Instructor", )
    session_ids = fields.Many2many(comodel_name="openacademy.session", relation="attendees_ids",
                                    string="Sessions", )
