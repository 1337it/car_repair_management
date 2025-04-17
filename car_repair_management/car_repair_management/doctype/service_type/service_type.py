# Copyright (c) 2024, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ServiceType(Document):
	
	def validate(self):
		self.create_service_item()
	
	def create_service_item(self):
		item = frappe.new_doc("Item")
		item.item_code = self.service_name
		item.item_name = self.service_name
		item.item_group = "Services"
		# item.standard_rate = self.price
		item.is_stock_item = 0

		item.insert()

