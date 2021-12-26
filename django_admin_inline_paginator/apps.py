# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoAdminInlinePaginatorConfig(AppConfig):
    name = 'django_admin_inline_paginator'
    verbose_name = _('Django Admin Inline Paginator')
