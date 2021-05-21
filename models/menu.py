from odoo import models, fields, api

class Menu(models.Model):
    _name = 'restaurantmng.menu'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    dish_ids = fields.Many2many('restaurantmng.dish', string="Dishes")
    drink_id = fields.Many2one('restaurantmng.drink', string="Drink", required=True)
    price = fields.Integer(compute='_calculate_price', string="Price (in €)")

    @api.depends('dish_ids', 'drink_id')
    def _calculate_price(self):
        for r in self:
            r.price = (sum(dish.price for dish in r.dish_ids) + r.drink_id.price)*0.8
