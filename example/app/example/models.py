# -*- coding: utf-8 -*-
from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              Model)


class Country(Model):
    name = CharField(max_length=100)
    active = BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class State(Model):
    country = ForeignKey('example.Country', on_delete=CASCADE)
    name = CharField(max_length=100)
    active = BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class Region(Model):
    country = ForeignKey('example.Country', on_delete=CASCADE)
    name = CharField(max_length=100)
    active = BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
