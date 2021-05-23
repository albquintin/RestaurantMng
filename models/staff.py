from odoo import models, fields, api, exceptions

class Staff(models.Model):
    _name = 'restaurantmng.staff'

    name = fields.Char(string="Name", required=True)
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
    working_area = fields.Selection([('management', 'Management'), ('marketing', 'Marketing'), ('team leader', 'Team Leader')], required=True)

class Chef(models.Model):
    _name = 'restaurantmng.chef'
    _inherit = 'restaurantmng.staff'

    specialty = fields.Char()
    dish_ids = fields.Many2many('restaurantmng.dish', string="Dishes")


class Service(models.Model):
    _name = 'restaurantmng.service'
    _inherit = 'restaurantmng.staff'

    area = fields.Selection([('bar', 'Bar'), ('terrace', 'Terrace'), ('tables', 'Tables')])

class Cleaning(models.Model):
    _name = 'restaurantmng.cleaning'
    _inherit = 'restaurantmng.staff'

    working_time = fields.Integer(string="Working Time (In h per week)")

class Delivery(models.Model):
    _name = 'restaurantmng.delivery'
    _inherit = 'restaurantmng.staff'

    own_vehicle = fields.Boolean()
    vehicle = fields.Selection([('motorcycle', 'Motorcycle'), ('bike', 'Bike'), ('car', 'Car')])

    @api.constrains('own_vehicle', 'vehicle')
    def _check_delivery_person_has_vehicle(self):
        for r in self:
            if not r.own_vehicle and r.vehicle:
                raise exceptions.ValidationError("Mark if the person has a vehicle before adding it")

