# -*- coding: utf-8 -*-
from openerp import http

# class PenyiapanJalur(http.Controller):
#     @http.route('/penyiapan_jalur/penyiapan_jalur/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/penyiapan_jalur/penyiapan_jalur/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('penyiapan_jalur.listing', {
#             'root': '/penyiapan_jalur/penyiapan_jalur',
#             'objects': http.request.env['penyiapan_jalur.penyiapan_jalur'].search([]),
#         })

#     @http.route('/penyiapan_jalur/penyiapan_jalur/objects/<model("penyiapan_jalur.penyiapan_jalur"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('penyiapan_jalur.object', {
#             'object': obj
#         })