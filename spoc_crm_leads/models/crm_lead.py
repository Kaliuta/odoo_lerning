from datetime import timedelta
from odoo import models, fields, api


class Lead(models.Model):
    _inherit = 'crm.lead'

    list_of_partners = fields.One2many('res.partner', compute='_compute_list_of_partners', string='List of partners',
                                       required=False)

    def _compute_list_of_partners(self):
        has_a_lead = self.env["crm.lead"].search([]).mapped("partner_id.id")
        system_users = self.env["res.users"].search([("groups_id", "=", self.env.ref("base.group_user").id)]
                                                    ).mapped("partner_id.id")

        compute_old_leads = self.env["crm.lead"].search(
            [("create_date", "<", fields.Date.today() - timedelta(days=28))]).mapped("partner_id.id")

        related_recordset = self.env["res.partner"].search(["&", ("id", "!=", system_users), "|",
                                                            ("id", "!=", has_a_lead),
                                                            ("id", "=", compute_old_leads), ])
        for record in self:
            record.list_of_partners = related_recordset

    @api.model
    def default_get(self, fields):
        res = super(Lead, self).default_get(fields)
        if self._context.get('active_id'):
            res['partner_id'] = self._context.get('active_id')
        return res


class Partner(models.Model):
    _inherit = 'res.partner'
    old_leads = fields.Boolean(compute='_compute_old_leads')

    def open_crm_form(self):
        return {
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
        }

    def _compute_old_leads(self):
        compute_old_leads = self.env["crm.lead"].search([("create_date", "<", fields.Date.today() - timedelta(days=28))]
                                                        ).mapped("partner_id.id")
        for record in self:
            record.old_leads = record.id in compute_old_leads
