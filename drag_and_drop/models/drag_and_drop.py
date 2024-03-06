# -*- coding: utf-8 -*-

from odoo import models, fields #, api

class drag_and_drop(models.Model):
    _name = 'fazteca.drag_and_drop'
    _description = 'Módulo para cargar archivos a ser procesados'

    column_1 = fields.Char(string='Column 1')
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):         
    #     for record in self:
    #         record.value2 = float(record.value) / 100

