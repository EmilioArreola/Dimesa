# -*- coding: utf-8 -*-
##############################################################################
#
#    A Cloud ERP Ltd.
#    Copyright (C) 2018-TODAY aCloudERP (<https://www.aclouderp.com>).
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL-3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL-3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL-3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Remove Powered by Odoo from Website, Email Template & Portal',
    'version': '18.0.1.6',
    'category': 'Website',
    'summary': 'This Odoo module focuses on removing default branding (remove powered by odoo create a free website ) elements such as "Powered by Odoo" from websites, portals, and footers. It offers a seamless solution for businesses aiming to personalize their Odoo instance and maintain a professional, white-labeled appearance. remove Powered by Odoo - The #1 Open Source eCommerce, hide Powered by Odoo - The #1 Open Source eCommerce, Remove Powered by Odoo,Remove Built with Odoo – The #1 Open Source Business App Suite,Remove Odoo: Open Source ERP & eCommerce Platform,Remove Odoo Website Builder – Build Your Site with Ease,Remove Made with ❤ using Odoo,Remove Odoo eCommerce – Modern, Fast, and Open Source',
    'description': """ 
    removed website powered by odoo
    remove powered by odoo from website footer 
    remove powered by odoo 17
    remove powered by odoo email 
    remove powered by odoo 18 
    remove website Debranding powered by, 
    remove powered by odoo create a free website 
    can i remove powered by odoo 
    uninstall odoo removal tool 
    Website Debranding,
    delete powered by odoo 
    delete odoo account 
    change powered by odoo 
    remove powered by odoo 14 
    how to remove powered by odoo 
    how to remove powered by odoo in website
    remove portal powered by,
    remove powered by odoo 16 
    remove powered by odoo 15 
    remove portal powered by odoo, 
    remove odoo powered by,
    remove powered by odoo 
    powered by odoo,
    Remove Powered by Odoo in Footer,
    Remove powered by in Odoo 17,
    Remove powered by in Odoo 16,
    Remove powered by in Odoo 15,
    turn off the "Powered by odoo" from website,
    Remove Powered by Odoo from Website footer,
    Remove Odoo branding, 
    remove powered by odoo from email template,
    removed powered by odoo from portal, 
    How to remove "Powered by Odoo" from the website footer,
    Disable "Powered by Odoo" in website and portal,
    Odoo website debranding – Remove Odoo branding,
    Remove "Powered by Odoo" in email templates,
    Turn off Powered by Odoo in Odoo 18, 17, 16, 15,
    Hide "Powered by Odoo" from customer portal,
    Odoo debranding guide – Remove Odoo branding,
    Customizing Odoo – Remove default footer branding,
    How to customize Odoo website and remove branding,
    Remove "Powered by Odoo" from invoices and emails,
    Odoo website customization – Remove footer text,
    Disable Odoo branding from website and portal,
    Hide Powered By Odoo,
    Remove Powered by Odoo in Footer on Website,
    how to remove the "powered by odoo" login page,
    Hide powered by odoo app,
    Remove powered by odoo from website footer,
    Remove Powered by Odoo 18,
    Remove Powered by Odoo 17,
    How to remove Powered by Odoo in email template,
    Remove powered by odoo 18 online,
    hide powered by odoo 18 online,
    Removing "Powered by Odoo" promotion message from an Odoo website,
    remove powered by odoo footer,
    odoo remove branding,
    remove odoo logo from website,
    hide odoo branding,
    delete powered by odoo,
    odoo website remove footer link,
    odoo 18 remove powered by,
    change powered by odoo text,
    odoo portal hide footer,
    odoo footer customization,
    how to hide powered by in odoo,
    remove odoo reference website,
    odoo remove powered by on portal,
    hide odoo footer link,
    odoo website remove copyright,
    odoo remove link from footer,
    remove odoo.com link from website,
    odoo website hide branding,
    odoo website remove default text,
    odoo backend remove branding,
    odoo 17 hide powered by odoo,
    odoo enterprise remove branding,
    remove powered by text from email,
    odoo remove branding from email templates,
    Powered by Odoo - The #1 Open Source eCommerce,
    remove Powered by Odoo - The #1 Open Source eCommerce,
    Remove Powered by Odoo,
    Remove Built with Odoo – The #1 Open Source Business App Suite,
    Remove Odoo: Open Source ERP & eCommerce Platform,
    Remove Odoo Website Builder – Build Your Site with Ease,
    Remove Made with ❤ using Odoo,
    Remove Odoo eCommerce – Modern, Fast, and Open Source,
""",
    'author': 'A Cloud ERP',
    'price': 15.00,
    'currency': "EUR",
    'website': 'http://www.aclouderp.com',
    'depends': ['auth_signup','website', 'portal'],
    'data': [
        'data/mail_template_data_portal_welcome.xml',
        'data/set_password_email.xml',
        'data/mail_template_user_signup_account_created.xml',
        'data/mail_notification_light.xml',
        'data/auth_signup_templates_email.xml',
        'data/digest_data.xml',
        'data/digest_tips_data.xml',
        'views/brand_promotion_message.xml',
        'views/portal_record_sidebar.xml',
    ],
    'installable': True,
    'auto_install': False,
    "images": ['static/description/banner.gif'],
    'license': 'OPL-1',
    'live_test_url': 'https://www.youtube.com/watch?v=IIEuXHaI2Ug',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
