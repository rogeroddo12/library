# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBook(models.Model):
    name = "library.book"


    name = fields.Char(String="Book")
    description = fields.Text(string="Description")






# class extra-addons/curso-odoo12/library(models.Model):
#     _name = 'extra-addons/curso-odoo12/library.extra-addons/curso-odoo12/library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
