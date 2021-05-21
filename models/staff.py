from odoo import models, fields

class Staff(models.Model):
    _name = 'restaurantmng.staff'

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    address = fields.Char()
    mobile_phone = fields.Char()
    salary = fields.Integer(string="Salary (in €, annual)")
    starting_date = fields.Date()

class Manager(models.Model):
    _name = 'restaurantmng.manager'
    _inherit = 'restaurantmng.staff'

    years_experience = fields.Integer()
    working_area = fields.Char()

class Chef(models.Model):
    _name = 'restaurantmng.chef'
    _inherit = 'restaurantmng.staff'

    specialty = fields.Char()
    dish_ids = fields.Many2many('restaurantmng.dish', string="Dishes")


class Service(models.Model):
    _name = 'restaurantmng.service'
    _inherit = 'restaurantmng.staff'

    area = fields.Selection([('bar', 'bar'), ('terrace', 'terrace')])

class Cleaning(models.Model):
    _name = 'restaurantmng.cleaning'
    _inherit = 'restaurantmng.staff'



class Delivery(models.Model):
    _name = 'restaurantmng.delivery'
    _inherit = 'restaurantmng.staff'

    own_vehicle = fields.Boolean()
    vehicle = fields.Selection([('motorcycle', 'Motorcycle'), ('bike', 'Bike'), ('car', 'Car')])

