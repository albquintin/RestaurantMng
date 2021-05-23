from odoo import models, fields, api, exceptions

class Supply_Order(models.Model):
  _name = 'restaurantmng.supply_order'

  order_number = fields.Integer(required=True)
  manager_id = fields.Many2one('restaurantmng.manager', string="Manager", required=True)
  order_date = fields.Date()
  total_price = fields.Integer()
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
          'message': 'Supply Order Confirmed',
          'type': 'rainbow_man',
        }
      }
            
  def action_done(self):
        for r in self:
            r.state = '3.done'

  def action_draft(self):
        for r in self:
            r.state = '1.draft'

class Food_Order(models.Model):
  _name = 'restaurantmng.food_order'
  _inherit = 'restaurantmng.supply_order'

  food_supplier_id = fields.Many2one('restaurantmng.food_supplier', string="Supplier", required=True)
  ingredient_ids = fields.Many2many('restaurantmng.ingredient', string="Ingredient", required=True)

  @api.constrains('food_supplier_id', 'ingredients_ids')
  def _check_supplier_supply_ingredient(self):
      for r in self:
          if r.ingredient_ids not in r.food_supplier_id.ingredient_ids:
              raise exceptions.ValidationError("The supplier doesn't supply this")

class Equipment_Order(models.Model):
  _name = 'restaurantmng.equipment_order'
  _inherit = 'restaurantmng.supply_order'

  equipment_supplier_id = fields.Many2one('restaurantmng.equipment_supplier', string="Supplier", required=True)
  equipment_ids = fields.Many2many('restaurantmng.equipment', string="Equipment", required=True)

  @api.constrains('equipment_supplier_id', 'equipment_ids')
  def _check_supplier_supply_equipment(self):
      for r in self:
          if r.equipment_ids not in r.equipment_supplier_id.equipment_ids:
              raise exceptions.ValidationError("The supplier doesn't supply this")

class Drink_Order(models.Model):
  _name = 'restaurantmng.drink_order'
  _inherit = 'restaurantmng.supply_order'

  drink_supplier_id = fields.Many2one('restaurantmng.drink_supplier', string="Supplier", required=True)
  drink_ids = fields.Many2many('restaurantmng.drink', string="Drink", required=True)

  @api.constrains('drink_supplier_id', 'drink_ids')
  def _check_supplier_supply_drink(self):
      for r in self:
          if r.drink_ids not in r.drink_supplier_id.drink_ids:
              raise exceptions.ValidationError("The supplier doesn't supply this")
