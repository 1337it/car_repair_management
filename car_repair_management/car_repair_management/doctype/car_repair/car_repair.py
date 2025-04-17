# Copyright (c) 2024, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CarRepair(Document):
	def validate(self):
		item_exist = frappe.db.exists("Item", {"name":self.service_type})
		if not item_exist:
			item = frappe.new_doc("Item")
			item.item_code = self.service_type
			item.item_name = self.service_type
			item.item_group = "Services"
			item.is_stock_item = 0

			item.insert()

		self.append_items()
	
	def append_items(self):
		if self.service_type:
			item = frappe.db.get_value("Car List Item", {"parent":self.name, "item_code": self.service_type}, "item_code")
			print(item)
			if not frappe.db.exists("Car List Item", {"parent":self.name, "item_code": self.service_type}):
				self.append("car_item_list",{
						"item_code": self.service_type,
						"qty":1,
					})
	
def validate(self,cdt):
	test_d = frappe.db.get_value("Vehicle",{'name':self.name},'name')
	if not test_d:
		vals = frappe.get_doc({
			"doctype": "Vehicle",
			"license_plate":self.name,
			"make":self.car_manufacturing_year,
			"model":self.car_model,
			"last_odometer": "0",
			"fuel_type": "Petrol",
			"uom": "Litre",
		})
		vals.insert()