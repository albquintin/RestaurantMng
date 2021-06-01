from odoo import models, fields, api, exceptions

class Drink(models.Model):
  _name = 'restaurantmng.drink'
  _order = 'name'

  name = fields.Char(string="Name", required=True)
  is_alcoholic = fields.Boolean()
  alcohol_volume = fields.Integer(string="º of alcohol")
  price = fields.Float(string="Price (in €)", required=True)

  @api.constrains('is_alcoholic', 'alcohol_volume')
  def _check_drink_is_alcoholic(self):
      for r in self:
          if not r.is_alcoholic and r.alcohol_volume:
              raise exceptions.ValidationError("Mark if the drink is alcoholic before adding the volume")

  @api.constrains('price')
  def _check_price_is_positive(self):
      for r in self:
          if r.price <= 0:
              raise exceptions.ValidationError("The price must be positive")