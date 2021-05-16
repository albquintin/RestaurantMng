from odoo import models, fields

class Order(models.Model):
  _name = 'restaurantmng.order'

  client_id = fields.Many2one('restaurantmng.client', string="Client", required=True)
  dish_ids = fields.Many2many('restaurantmng.dish', string="Dishes")
  menu_ids = fields.Many2many('restaurantmng.menu', string="Menus")
  delivery_id = fields.Many2one('restaurantmng.delivery', string="Delivery Person", required=True)

