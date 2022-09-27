from projeto_advocacia.core.apps import CoreConfig


def test_app_name():
    assert CoreConfig.name == 'projeto_advocacia.core'
