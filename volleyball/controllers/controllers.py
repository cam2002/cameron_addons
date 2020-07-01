# -*- coding: utf-8 -*-
from odoo import http

# class Volleyball(http.Controller):
#     @http.route('/volleyball/volleyball/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/volleyball/volleyball/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('volleyball.listing', {
#             'root': '/volleyball/volleyball',
#             'objects': http.request.env['volleyball.volleyball'].search([]),
#         })

#     @http.route('/volleyball/volleyball/objects/<model("volleyball.volleyball"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('volleyball.object', {
#             'object': obj
#         })