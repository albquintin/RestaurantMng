from odoo import models, fields

class Menu(models.Model):
    _name = 'restaurantmng.menu'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    dish_ids = fields.Many2many('restaurantmng.dish', string="Dishes")
    price = fields.Integer(string="Price (in €)")
