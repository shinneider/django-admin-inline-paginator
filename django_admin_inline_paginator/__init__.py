# -*- coding: utf-8 -*-
from django import __version__ as django_version

if django_version < '3.2':  # pragma: no cover
    default_app_config = 'django_admin_inline_paginator.apps.DjangoAdminInlinePaginatorConfig'
