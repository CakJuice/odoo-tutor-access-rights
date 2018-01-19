# -*- coding: utf-8 -*-
from odoo import http

# class CjTutorAccessRight(http.Controller):
#     @http.route('/cj_tutor_access_right/cj_tutor_access_right/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cj_tutor_access_right/cj_tutor_access_right/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cj_tutor_access_right.listing', {
#             'root': '/cj_tutor_access_right/cj_tutor_access_right',
#             'objects': http.request.env['cj_tutor_access_right.cj_tutor_access_right'].search([]),
#         })

#     @http.route('/cj_tutor_access_right/cj_tutor_access_right/objects/<model("cj_tutor_access_right.cj_tutor_access_right"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cj_tutor_access_right.object', {
#             'object': obj
#         })