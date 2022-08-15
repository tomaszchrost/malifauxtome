from . import models
from django import forms
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from pdf2image import convert_from_bytes


class StatCardAdmin(models.StatCard):

    list_display = ('name', 'test')


admin.site.register(models.StatCard)


class KeywordAdmin(models.Keyword):

    list_display = ('name',)


admin.site.register(models.Keyword)


class MalifauxModelAdmin(models.MalifauxModel):

    list_display = ('name',)


admin.site.register(models.MalifauxModel)

admin.site.register(models.Faction)
admin.site.register(models.Ability)
admin.site.register(models.Action)
admin.site.register(models.Trigger)
admin.site.register(models.Characteristic)
