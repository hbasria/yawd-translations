# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(choices=[('af', 'Afrikaans'), ('sq', 'Albanian'), ('ar', 'Arabic'), ('es-ar', 'Argentinian Spanish'), ('ast', 'Asturian'), ('en-au', 'Australian English'), ('az', 'Azerbaijani'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('pt-br', 'Brazilian Portuguese'), ('br', 'Breton'), ('en-gb', 'British English'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('ca', 'Catalan'), ('es-co', 'Colombian Spanish'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('kn', 'Kannada'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('ko', 'Korean'), ('lv', 'Latvian'), ('lt', 'Lithuanian'), ('dsb', 'Lower Sorbian'), ('lb', 'Luxembourgish'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('es-mx', 'Mexican Spanish'), ('mn', 'Mongolian'), ('ne', 'Nepali'), ('es-ni', 'Nicaraguan Spanish'), ('nb', 'Norwegian Bokmål'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('fa', 'Persian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('ro', 'Romanian'), ('ru', 'Russian'), ('gd', 'Scottish Gaelic'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('zh-hans', 'Simplified Chinese'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('es', 'Spanish'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('zh-hant', 'Traditional Chinese'), ('tr', 'Turkish'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('hsb', 'Upper Sorbian'), ('ur', 'Urdu'), ('es-ve', 'Venezuelan Spanish'), ('vi', 'Vietnamese'), ('cy', 'Welsh')], max_length=7, primary_key=True, serialize=False, verbose_name='Name')),
                ('image', models.CharField(blank=True, max_length=100, null=True, verbose_name='Image')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'verbose_name_plural': 'Languages',
                'verbose_name': 'Language',
                'permissions': (('view_translations', 'Can see translation messages for a language'), ('edit_translations', "Can edit the language's translation messages")),
                'ordering': ['order', 'name'],
            },
        ),
    ]
