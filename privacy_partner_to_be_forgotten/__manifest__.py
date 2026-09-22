# Copyright (C) 2025 Cetmix OÜ
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Privacy Partner's Right to be Forgotten",
    "version": "18.0.1.0.0",
    "development_status": "Beta",
    "category": "Data Protection",
    "summary": "Anonymize partner data for GDPR compliance",
    "author": "Cetmix, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "website": "https://vertel.se/apps/odoo-oca-data-protection/privacy_partner_to_be_forgotten",
    "depends": ["contacts"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "wizards/partner_anonymize_wizard_views.xml",
    ],
    "demo": ["demo/demo_partner_anonymize_data.xml"],
}
