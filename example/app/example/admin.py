from django.contrib.admin import ModelAdmin, register
from django_admin_inline_paginator.admin import TabularInlinePaginated, InlineModelPaginated

from .models import Country, Region, State


class StateAdminInline(TabularInlinePaginated):
    fields = ('name', 'active')
    per_page = 5
    model = State


class RegionAdminInline(TabularInlinePaginated):
    fields = ('name', 'active')
    per_page = 2
    model = Region
    pagination_key = 'rpage'


@register(Country)
class CountryAdmin(InlineModelPaginated, ModelAdmin):
    fields = ('name', 'active')
    inlines = (StateAdminInline, RegionAdminInline)
    inline_pagination_keys = (StateAdminInline.pagination_key, RegionAdminInline.pagination_key)
    model = Country
