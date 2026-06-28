import requests
from flask import current_app
from markupsafe import Markup

VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"


class RecaptchaService:
    """Google reCAPTCHA v2 — a CAPTCHA that protects forms from spam.

    A utility service with no DB model. Registered under the generic
    ``CaptchaService`` name (the alternative to cloudflare). Templates use the
    captcha_widget()/captcha_script() helpers; routes call verify() before
    accepting a submission.
    """

    def site_key(self):
        return current_app.config.get("RECAPTCHA_SITE_KEY", "")

    def enabled(self):
        return bool(self.site_key())

    def widget(self):
        key = self.site_key()
        if not key:
            return Markup("")
        return Markup(f'<div class="g-recaptcha" data-sitekey="{key}"></div>')

    def script_tag(self):
        if not self.enabled():
            return Markup("")
        return Markup(
            '<script src="https://www.google.com/recaptcha/api.js"'
            " async defer></script>"
        )

    def verify(self, token, remoteip=None):
        secret = current_app.config.get("RECAPTCHA_SECRET_KEY", "")
        if not secret:
            return True
        if not token:
            return False
        try:
            data = {"secret": secret, "response": token}
            if remoteip:
                data["remoteip"] = remoteip
            resp = requests.post(VERIFY_URL, data=data, timeout=10)
            return bool(resp.json().get("success"))
        except Exception:
            return False
