from odoo import models, fields

class Equipment(models.Model):
    _name = 'restaurantmng.equipment'

    name = fields.Char(string="Name", required=True)
    brand = fields.Char()
    buying_date = fields.Date()
    price = fields.Integer()
    