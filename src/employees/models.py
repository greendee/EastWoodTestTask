from django.core.urlresolvers import reverse
from django.db import models


class Employee(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

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

    def __str__(self):
        return "%s %s %s, %s" % (self.surname, self.name, self.patronymic, self.position)

    def get_url(self):
        return reverse('employees:employee:detail', kwargs={'pk': self.pk})


class Department(models.Model):
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return "Отдел %s" % self.name

    def get_url(self):
        return reverse('employees:department:detail', kwargs={'pk': self.pk})
