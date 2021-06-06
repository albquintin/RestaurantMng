from odoo import models, fields

class Neighborhood(models.Model):
  _name = 'restaurantmng.neighborhood'
  _order = 'name'

  name = fields.Char(string="Name", required=True)
  postcode = fields.Integer()
  population = fields.Integer()


