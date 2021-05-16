from odoo import models, fields

class Event(models.Model):
  _name = 'restaurantmng.event'

  event_date = fields.Date()
  num_people = fields.Integer()
  service_ids = fields.Many2many('restaurantmng.service', string="Service People")
  chef_ids = fields.Many2many('restaurantmng.chef', string="Chefs")