from odoo import models, fields

class Client(models.Model):
    _name = 'restaurantmng.client'

    name = fields.Char(string="Name", required=True)
    surname = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    neighborhood_id = fields.Many2one('restaurantmng.neighborhood', string="Neighborhood", required=True)
    is_vip = fields.Boolean()

