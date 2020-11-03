import unittest
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django_admin_inline_paginator.apps import DjangoAdminInlinePaginatorConfig


class TestDjangoAppConfig(unittest.TestCase):

    def test_valid_subclass_appconfig(self):
        self.assertEqual(issubclass(DjangoAdminInlinePaginatorConfig, AppConfig), True)

    def test_valid_name(self):
        name = DjangoAdminInlinePaginatorConfig.name
        self.assertEqual(isinstance(name, str), True)
        self.assertEqual(name, 'django_admin_inline_paginator')

    def test_valid_verbose_name(self):
        verbose_name = DjangoAdminInlinePaginatorConfig.verbose_name
        self.assertEqual(verbose_name, _('Django Admin Inline Paginator'))
