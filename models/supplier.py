from odoo import models, fields

class Supplier(models.Model):
  _name = 'restaurantmng.supplier'
  _order = 'name'

  name = fields.Char(string="Name", required=True)
  contact_person = fields.Char()
  address = fields.Char()
  email = fields.Char()

class Food_Supplier(models.Model):
  _name = 'restaurantmng.food_supplier'
  _inherit = 'restaurantmng.supplier'

  ingredient_ids = fields.Many2many('restaurantmng.ingredient', string="Ingredients")

class Equipment_Supplier(models.Model):
  _name = 'restaurantmng.equipment_supplier'
  _inherit = 'restaurantmng.supplier'

  equipment_ids = fields.Many2many('restaurantmng.equipment', string="Equipment") 

class Drink_Supplier(models.Model):
  _name = 'restaurantmng.drink_supplier'
  _inherit = 'restaurantmng.supplier'

  drink_ids = fields.Many2many('restaurantmng.drink', string="Drinks") 


