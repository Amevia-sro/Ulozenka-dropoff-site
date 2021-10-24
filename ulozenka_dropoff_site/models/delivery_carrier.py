from odoo import fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    dropoff_site = fields.Boolean('Dropoff Site')
    partner_ids = fields.Many2many('res.partner', string='Site Addresses')
