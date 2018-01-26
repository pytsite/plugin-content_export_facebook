"""PytSite Facebook Content Export Driver
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_uwsgi():
    from plugins import content_export
    from . import _driver

    content_export.register_driver(_driver.Driver())
