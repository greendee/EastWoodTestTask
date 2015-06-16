from django.db import models


class Employee(models.Model):
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    date_work_start = models.DateField(auto_created=True, verbose_name='Дата начала работы')
    date_work_end = models.DateField(default=None, null=True, blank=True, verbose_name='Дата окончания работы')
    position = models.CharField(max_length=255, verbose_name='Должность')
    department = models.ForeignKey('Department', verbose_name='Отдел')


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')


