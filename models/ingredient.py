from odoo import models, fields

class Ingredient(models.Model):
  _name = 'restaurantmng.ingredient'
  _order = 'name'

  name = fields.Char(string="Name", required=True)