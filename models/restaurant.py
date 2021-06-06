from odoo import models, fields

class Restaurant(models.Model):
    _name = 'restaurantmng.restaurant'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    founder = fields.Char(string="Name of the founder")
    city = fields.Char()
    country = fields.Char()
    color = fields.Integer()
    restaurant_image = fields.Binary(string="Restaurant Image", max_width=100, max_height=100, 
                            verify_resolution=False)