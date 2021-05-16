from odoo import models, fields

class Supply_Order(models.Model):
  _name = 'restaurantmng.supply_order'

  manager_id = fields.Many2one('restaurantmng.manager', string="Manager", required=True)
  order_date = fields.Date()
  total_price = fields.Integer()

class Food_Order(models.Model):
  _name = 'restaurantmng.food_order'
  _inherit = 'restaurantmng.supply_order'

  food_supplier_id = fields.Many2one('restaurantmng.food_supplier', string="Supplier", required=True)
  ingredient_ids = fields.Many2many('restaurantmng.ingredient', string="Ingredient", required=True)

class Equipment_Order(models.Model):
  _name = 'restaurantmng.equipment_order'
  _inherit = 'restaurantmng.supply_order'

  equipment_supplier_id = fields.Many2one('restaurantmng.equipment_supplier', string="Supplier", required=True)
  equipment_ids = fields.Many2many('restaurantmng.equipment', string="Equipment", required=True)

class Drink_Order(models.Model):
  _name = 'restaurantmng.drink_order'
  _inherit = 'restaurantmng.supply_order'

  drink_supplier_id = fields.Many2one('restaurantmng.drink_supplier', string="Supplier", required=True)
  drink_ids = fields.Many2many('restaurantmng.drink', string="Drink", required=True)

