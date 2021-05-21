from odoo import models, fields, api

class Order(models.Model):
  _name = 'restaurantmng.order'

  order_number = fields.Integer(required=True)
  client_id = fields.Many2one('restaurantmng.client', string="Client", required=True)
  dish_ids = fields.Many2many('restaurantmng.dish', string="Dishes")
  menu_ids = fields.Many2many('restaurantmng.menu', string="Menus")
  drink_ids = fields.Many2many('restaurantmng.drink', string="Drinks")
  delivery_id = fields.Many2one('restaurantmng.delivery', string="Delivery Person", required=True)
  address = fields.Char()
  neighborhood = fields.Char(compute='_get_neighborhood')
  total_price = fields.Integer(compute='_calculate_price')

  @api.depends('dish_ids', 'menu_ids', 'drink_ids')
  def _calculate_price(self):
      for r in self:
          r.total_price = sum(dish.price for dish in r.dish_ids) + sum(menu.price for menu in r.menu_ids) + sum(drink.price for drink in r.drink_ids)

  @api.depends('client_id')
  def _get_neighborhood(self):
      for r in self:
          r.neighborhood = r.client_id.neighborhood_id.name
