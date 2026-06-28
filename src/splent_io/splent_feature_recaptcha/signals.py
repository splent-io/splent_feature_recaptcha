"""Anti-spam: validate submitted comments with Google reCAPTCHA.

Listens to the comments feature's ``comment-submitting`` signal. No hard
dependency on comments — if comments isn't installed the signal is never
defined and this handler is simply skipped.
"""

from splent_framework.signals.signal_utils import connect_signal


@connect_signal("comment-submitting", "splent_feature_recaptcha")
def validate_recaptcha(sender, form=None, remoteip=None, **kwargs):
    from splent_io.splent_feature_recaptcha.services import RecaptchaService

    token = form.get("g-recaptcha-response") if form else None
    return RecaptchaService().verify(token, remoteip)


@connect_signal("contact-submitting", "splent_feature_recaptcha")
def validate_recaptcha_contact(sender, form=None, remoteip=None, **kwargs):
    from splent_io.splent_feature_recaptcha.services import RecaptchaService

    token = form.get("g-recaptcha-response") if form else None
    return RecaptchaService().verify(token, remoteip)
