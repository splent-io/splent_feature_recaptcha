"""Google reCAPTCHA v2 configuration (anti-spam CAPTCHA).

Set RECAPTCHA_SITE_KEY / RECAPTCHA_SECRET_KEY in the product's .env (dev/prod),
or configure them from the admin panel. Defaults are Google's official TEST
keys (always pass), so development works out of the box.
"""

import os

# Google's documented reCAPTCHA v2 test keys: always pass, safe for dev.
_TEST_SITE_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
_TEST_SECRET_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"


def inject_config(app):
    app.config.update(
        {
            "RECAPTCHA_SITE_KEY": os.getenv("RECAPTCHA_SITE_KEY", _TEST_SITE_KEY),
            "RECAPTCHA_SECRET_KEY": os.getenv(
                "RECAPTCHA_SECRET_KEY", _TEST_SECRET_KEY
            ),
        }
    )
