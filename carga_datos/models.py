# -*- coding: utf-8 -*-

from odoo import models, fields, api


class carga_datos(models.Model):
    _name = 'carga.datos'
    _description = 'Carga de datos para el dashboard de Fuego Azteca'

    name = fields.Char()