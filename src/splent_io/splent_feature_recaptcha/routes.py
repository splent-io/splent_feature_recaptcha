from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from splent_io.splent_feature_recaptcha import recaptcha_bp
from splent_framework.services.service_locator import service_proxy

# Setting keys edited by the Captcha settings panel.
CAPTCHA_FIELDS = [
    "recaptcha_site_key",
    "recaptcha_secret_key",
]


@recaptcha_bp.route("/admin/captcha", methods=["GET", "POST"])
@login_required
def admin_settings():
    """Captcha settings panel for Google reCAPTCHA.

    Edits the site/secret keys and persists them via SettingsService. The
    RecaptchaService reads these keys back, so changes apply immediately.
    """
    if request.method == "POST":
        values = {field: request.form.get(field, "") for field in CAPTCHA_FIELDS}
        service_proxy("SettingsService").set_many(values)
        flash("Captcha settings updated.", "success")
        return redirect(url_for("recaptcha.admin_settings"))

    return render_template("recaptcha/admin/settings.html")
