# -*- coding: utf-8 -*-
# from odoo import http


# class DragAndDrop(http.Controller):
#     @http.route('/drag_and__drop/drag_and__drop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drag_and__drop/drag_and__drop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('drag_and__drop.listing', {
#             'root': '/drag_and__drop/drag_and__drop',
#             'objects': http.request.env['drag_and__drop.drag_and__drop'].search([]),
#         })

#     @http.route('/drag_and__drop/drag_and__drop/objects/<model("drag_and__drop.drag_and__drop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drag_and__drop.object', {
#             'object': obj
#         })

