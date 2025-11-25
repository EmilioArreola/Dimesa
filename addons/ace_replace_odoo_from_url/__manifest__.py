# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Remove Odoo from URLs | Replace Odoo URL | Remove Odoo from URL | Remove Odoo URL',
    'version' : '18.0.1.2',
    'summary': """ 
        Looking to replace or remove /odoo from your website URL? Our premium Odoo module offers a seamless solution to clean up and customize your Odoo URLs for a professional look. 
        Eliminate the default /odoo/ path and boost your brand credibility with user-friendly, SEO-optimized URLs. Perfect for businesses aiming to improve their Odoo website experience, 
        our module works with odoo 18 and configurations. Easy to install, fully documented, and backed by expert support—buy now and give your Odoo site the clean, custom URLs it deserves. 
        Ideal for developers, agencies, and Odoo service providers, replace odoo in URL, remove odoo url, oodo url.
    """,
    'sequence': 10,
    'description': """
        replace "odoo" in URL
        remove "odoo" from URL
        odoo URL cleanup
        change odoo URL path
        customize Odoo URL
        remove /odoo/ from web URL
        rewrite Odoo base URL
        Odoo URL rewrite rules
        odoo website URL remove prefix
        nginx remove odoo from URL
        odoo 18 remove /odoo from URL
        how to remove /odoo/ from Odoo website URL
        replace /odoo/ with / in Odoo URL
        clean Odoo URLs without /odoo/ path
        Odoo remove default /odoo/ route from URLs
        rewrite URL to remove odoo prefix in Odoo
        Odoo base path customization remove /odoo/
        remove odoo path from website URL
        Odoo change root URL from /odoo to /
        How to change page URL in Odoo
    """,
    'category': 'Extra Tools',
    'author': 'A Cloud ERP',
    'website': 'https://www.aclouderp.com',
    'images' : ['static/description/banner.png'],
    'depends' : ["web",'base'],
    'price': 9.0,
    'currency': "USD",
    'live_test_url': 'https://www.youtube.com/watch?v=4zh0FwcpSHw',
    'data': [
        'data/data.xml',
        'views/ir_config_parameter.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "ace_replace_odoo_from_url/static/src/js/web_url_replace_view.js"
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
    'uninstall_hook': '_uninstall_cleanup',
}
