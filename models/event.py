from odoo import models, fields

class Event(models.Model):
  _name = 'restaurantmng.event'

  name = fields.Char(string="Name", required=True)
  event_date = fields.Date(required=True)
  num_people = fields.Integer()
  service_ids = fields.Many2many('restaurantmng.service', string="Service People")
  chef_ids = fields.Many2many('restaurantmng.chef', string="Chefs")
  color = fields.Integer()
  state = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')

  
  def action_confirm(self):
    for r in self:
      r.state = '2.confirm'
      return {
        'effect': {
          'fadeout': 'slow',
          'message': 'Event Confirmed',
          'type': 'rainbow_man',
        }
      }
            
  def action_done(self):
        for r in self:
            r.state = '3.done'

  def action_draft(self):
        for r in self:
            r.state = '1.draft'