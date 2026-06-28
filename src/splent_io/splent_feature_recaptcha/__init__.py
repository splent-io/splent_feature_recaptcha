from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.services.service_locator import register_service, service_proxy

from splent_io.splent_feature_recaptcha.services import RecaptchaService

recaptcha_bp = create_blueprint(__name__)


def init_feature(app):
    # Generic "CaptchaService" name so consumers stay provider-agnostic; this is
    # the Google reCAPTCHA implementation of the 'captcha' alternative.
    register_service(app, "CaptchaService", RecaptchaService)


def inject_context_vars(app):
    def captcha_widget():
        return service_proxy("CaptchaService").widget()

    def captcha_script():
        return service_proxy("CaptchaService").script_tag()

    return {"captcha_widget": captcha_widget, "captcha_script": captcha_script}
