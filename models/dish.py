from odoo import models, fields

class Dish(models.Model):
    _name = 'restaurantmng.dish'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    dish_type = fields.Selection([('starter', 'Starter'), ('main_course', 'Main Course'), ('dessert', 'Dessert')])
    ingredient_ids = fields.Many2many('restaurantmng.ingredient', string="Ingredients")
    is_vegan = fields.Boolean()
    price = fields.Integer(string="Price (in €)")


