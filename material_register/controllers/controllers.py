# -*- coding: utf-8 -*-
# from odoo import http


# class MaterialRegister(http.Controller):
#     @http.route('/material_register/material_register/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/material_register/material_register/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('material_register.listing', {
#             'root': '/material_register/material_register',
#             'objects': http.request.env['material_register.material_register'].search([]),
#         })

#     @http.route('/material_register/material_register/objects/<model("material_register.material_register"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('material_register.object', {
#             'object': obj
#         })
