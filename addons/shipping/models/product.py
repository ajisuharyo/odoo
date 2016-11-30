# -*- coding: utf-8 -*-
from datetime import date #) ini harus di import apabila ada field date & datetime pada tabel model database
from openerp import models, fields, api #) wajib iye mh titik
from openerp.exceptions import ValidationError #) ini harus di import apabila akan memunculkan error message

class product(models.Model):
	_name = 'shipping.products' #) nama ini akan menjadi nama tabel, bisa di relasikan dengan model lain. eg: shipping.route
	_rec_name = 'name' #) ini untuk breadcumb
	_description = "Master data Produk Penyiapan Jalur"
	_sql_constraints = [('code_uniq', 'unique(code)', "Judul Harus Uniq Bro !!")]

	name = fields.Char(string='Nama Produk', required=True, select=1, index=True)
	code = fields.Char(string='Kode Produk', help='buat kolom kode bro..')
	is_not_ppn = fields.Boolean(string='Bebas PPN', default=True, help='true false juga boleh')
	last_purchase_price = fields.Float(digits=(10, 5))
	default_discount = fields.Float(digits=(10, 5), default='0')
	last_purchase_price = fields.Float(digits=(10, 5))
	point = fields.Integer(string='Poin', default='1')
	type_product = fields.Selection([('Persediaan', 'Persediaan'), ('Aset', 'Aset'), ('Meneketehe', 'Meneketehe')], 'Type Produk')
	status = fields.Boolean(string='Status', default=True, help='delete udah di hapus bearti')
	description = fields.Text(string='Keterangan', help='ini buat isi keterangan') #) help bila di hover, akan memunculkan isi message nya




