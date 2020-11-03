from django.contrib.admin import register, ModelAdmin
from django_admin_inline_paginator.admin import TabularInlinePaginated

from .models import Country, State


class StateAdminInline(TabularInlinePaginated):
    fields = ('name', 'active')
    per_page = 1
    model = State


@register(State)
class StateAdmin(ModelAdmin):
    fields = ('country', 'name', 'active')
    model = State


@register(Country)
class CountryAdmin(ModelAdmin):
    fields = ('name', 'active')
    inlines = (StateAdminInline, )
    model = Country
