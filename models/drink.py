from odoo import models, fields

class Drink(models.Model):
  _name = 'restaurantmng.drink'
  _order = 'name'

  name = fields.Char(string="Name", required=True)
  is_alcoholic = fields.Boolean()
  alcohol_volume = fields.Integer(string="º of alcohol")
  price = fields.Integer(string="Price (in €)")