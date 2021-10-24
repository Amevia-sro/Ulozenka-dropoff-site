{
    'name': 'Ulozenka eCommerce Delivery (Dropoff Sites)',
    'category': 'Website/Website',
    'author': 'Amevia s.r.o.',
    "website" : "https://www.amevia.eu",
    'summary': 'Enable dropoff sites configuration on shipping methods by Ulozenka.',
    'version': '1.0',
    'depends': ['website_sale_delivery'],
    'data': [
        'views/delivery_view.xml',
        'views/website_sale_delivery_templates.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': True,
}
