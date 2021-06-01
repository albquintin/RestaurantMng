from odoo import models, fields, api, exceptions
from datetime import date

class Equipment(models.Model):
  _name = 'restaurantmng.equipment'

  name = fields.Char(string="Name", required=True)
  brand = fields.Char(required=True)
  buying_date = fields.Date(required=True)
  price = fields.Float(required=True)
  years_of_use = fields.Integer(compute='_calculate_years_of_use', string="Years of Use")

  @api.depends('buying_date')
  def _calculate_years_of_use(self):
    for r in self:
      today = date.today()
      r.years_of_use = ((today-r.buying_date).days)/365

  @api.constrains('price')
  def _check_price_is_positive(self):
    for r in self:
        if r.price <= 0:
            raise exceptions.ValidationError("The price must be positive")
    