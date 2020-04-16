# -*- coding: utf-8 -*-
# from odoo import http


# class Tech1Custom(http.Controller):
#     @http.route('/tech1_custom/tech1_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech1_custom/tech1_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech1_custom.listing', {
#             'root': '/tech1_custom/tech1_custom',
#             'objects': http.request.env['tech1_custom.tech1_custom'].search([]),
#         })

#     @http.route('/tech1_custom/tech1_custom/objects/<model("tech1_custom.tech1_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech1_custom.object', {
#             'object': obj
#         })
