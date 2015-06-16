# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_work_start', models.DateField(verbose_name='Дата начала работы', auto_created=True)),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=255)),
                ('name', models.CharField(verbose_name='Имя', max_length=255)),
                ('patronymic', models.CharField(verbose_name='Отчество', max_length=255)),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=255)),
                ('date_work_end', models.DateField(blank=True, verbose_name='Дата окончания работы', default=None, null=True)),
                ('position', models.CharField(verbose_name='Должность', max_length=255)),
                ('department', models.ForeignKey(to='employees.Department', verbose_name='Отдел')),
            ],
        ),
    ]
