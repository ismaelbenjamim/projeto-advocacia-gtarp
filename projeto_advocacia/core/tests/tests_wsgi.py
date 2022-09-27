import os

from django.core.handlers.wsgi import WSGIHandler

from projeto_advocacia.wsgi import application


def test_wsgi_default_settings():
    assert 'projeto_advocacia.settings' == os.environ["DJANGO_SETTINGS_MODULE"]


def test_application_instance():
    assert isinstance(application, WSGIHandler)
