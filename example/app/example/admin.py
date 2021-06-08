from django.contrib.admin import ModelAdmin, register
from django_admin_inline_paginator.admin import TabularInlinePaginated

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
class CountryAdmin(ModelAdmin):
    fields = ('name', 'active')
    inlines = (StateAdminInline, RegionAdminInline)
    model = Country
