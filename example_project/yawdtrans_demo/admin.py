from django.contrib import admin
from models import MultilingualPage, MultilingualPageTranslation

from translations.admin import TranslationInline


class MultilingualPageTranslationAdmin(TranslationInline):
    model = MultilingualPageTranslation


class MultilingualPageAdmin(admin.ModelAdmin):
    inlines = [MultilingualPageTranslationAdmin]


admin.site.register(MultilingualPage, MultilingualPageAdmin)
