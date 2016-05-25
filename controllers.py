# -*- coding: utf-8 -*-
from openerp import http

# class ModuloPartidos(http.Controller):
#     @http.route('/modulo_partidos/modulo_partidos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_partidos/modulo_partidos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_partidos.listing', {
#             'root': '/modulo_partidos/modulo_partidos',
#             'objects': http.request.env['modulo_partidos.modulo_partidos'].search([]),
#         })

#     @http.route('/modulo_partidos/modulo_partidos/objects/<model("modulo_partidos.modulo_partidos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_partidos.object', {
#             'object': obj
#         })