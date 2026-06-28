from flask import request, url_for

from splent_framework.hooks.template_hooks import register_template_hook


def recaptcha_admin_link():
    """Sidebar entry for the Captcha settings screen (the WP-plugin pattern)."""
    active = (
        "active"
        if request.endpoint and request.endpoint.startswith("recaptcha.admin")
        else ""
    )
    return (
        f'<li class="sidebar-item {active}">'
        f'<a class="sidebar-link" href="{url_for("recaptcha.admin_settings")}">'
        '<i class="align-middle" data-feather="shield"></i> '
        '<span class="align-middle">Captcha</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.authenticated_sidebar", recaptcha_admin_link)
