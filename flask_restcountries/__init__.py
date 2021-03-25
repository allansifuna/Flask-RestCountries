from flask import Blueprint, current_app
from restcountries import RestCountryApiV2


class CountriesAPI(RestCountryApiV2):
    def __init__(self, app=None, **kwargs):

        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.register_blueprint(app)

    @staticmethod
    def register_blueprint(app):
        module = Blueprint('restcountriesapi', __name__,
                           template_folder='templates')
        app.register_blueprint(module)
        return module

    def get_app(self, reference_app=None):
        """Helper method that implements the logic to look up an
        application."""

        if reference_app is not None:
            return reference_app

        if current_app:
            return current_app._get_current_object()

        if self.app is not None:
            return self.app

        raise RuntimeError(
            'No application found. Either work inside a view function or push'
            ' an application context.'
        )

    # @property
    # def CountriesAPI(self):
    #     return RestCountryApiV2
