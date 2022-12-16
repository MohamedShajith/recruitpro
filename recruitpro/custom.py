from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def login_page_popup():
    if frappe.session.user == "mohamedshajith.j@groupteampro.com":
        frappe.msgprint(
            'Welcome to our page RECRUITPRO',
        )

