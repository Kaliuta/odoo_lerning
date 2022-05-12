
from odoo import models, fields

class CHAStockQuant(models.Model):
    _inherit = 'stock.quant'

    product_categ_id = fields.Many2one(store=True)

