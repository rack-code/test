# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tech1_custom(models.Model):
#     _name = 'tech1_custom.tech1_custom'
#     _description = 'tech1_custom.tech1_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
