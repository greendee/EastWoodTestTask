from django import forms
from . import models
from django.forms import widgets


class EmployeeListFilterForm(forms.Form):
    department = forms.ModelChoiceField(queryset=models.Department.objects.all().order_by('name'), label='Отдел',
                                        widget=widgets.Select(attrs={"class": "form-control"})
                                        )
    still_working = forms.BooleanField(label="Работает", required=False,
                                       widget=widgets.CheckboxInput(attrs={"class": "form-control"}))

    def clean(self):
        data = super().clean()
        works = data.pop('still_working', False)
        if works:
            data['date_work_end__isnull'] = True
        return data