from odoo import models, fields, api


class CreateSession(models.TransientModel):
    _name = 'fill.session.wizard'
    _description = 'Session fill wizard'
    session_ids = fields.Many2many(comodel_name="openacademy.session", string="Session", )
    attendees_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")

    @api.model
    def default_get(self, _fields):
        """ Use active_ids from the context to fetch the leads/opps to merge.
            In order to get merged, these leads/opps can't be in 'Dead' or 'Closed'
        """
        result = super(CreateSession, self).default_get(_fields)
        result['session_ids'] = self.env['openacademy.session'].browse(self._context.get('active_id'))
        return result

    def action_fill_attendees(self):
        return self.session_ids.action_fill_attendees(attendees_ids=self.attendees_ids)
