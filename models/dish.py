from odoo import models, fields, api, exceptions

class Dish(models.Model):
    _name = 'restaurantmng.dish'
    _order = 'name'

    name = fields.Char(string="Name", required=True)
    dish_type = fields.Selection([('starter', 'Starter'), ('main_course', 'Main Course'), ('dessert', 'Dessert')], required=True)
    ingredient_ids = fields.Many2many('restaurantmng.ingredient', string="Ingredients", required=True)
    is_vegan = fields.Boolean()
    non_gluten = fields.Boolean()
    spicy = fields.Boolean()
    price = fields.Float(string="Price (in €)", required=True)

    @api.constrains('price')
    def _check_price_is_positive(self):
        for r in self:
            if r.price <= 0:
                raise exceptions.ValidationError("The price must be positive")


