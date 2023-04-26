# -*- coding: utf-8 -*-
try:
    import django

    if django.VERSION < (3, 2):  # pragma: no cover
        default_app_config = 'django_admin_inline_paginator.apps.DjangoAdminInlinePaginatorConfig'
except ImportError:
    pass
