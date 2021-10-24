from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleExtended(WebsiteSale):

    @http.route(['/shop/update_shipping'], type='http', auth="public", website=True, sitemap=False)
    def update_shipping_to_dropoff_site(self, **post):
        order = request.website.sale_get_order()
        order['partner_shipping_id'] = int(post['partner_id'])
        return request.redirect('/shop/payment')
