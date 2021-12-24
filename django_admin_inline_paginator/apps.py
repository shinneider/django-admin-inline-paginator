# -*- coding: utf-8 -*-
from django.apps import AppConfig
try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


class DjangoAdminInlinePaginatorConfig(AppConfig):
    name = 'django_admin_inline_paginator'
    verbose_name = _('Django Admin Inline Paginator')
