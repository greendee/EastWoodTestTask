from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils.functional import cached_property
from django.views import generic

from . import models, forms


class DepartmentDetailView(generic.DetailView):
    model = models.Department


class DepartmentListView(generic.ListView):
    paginate_by = 20
    queryset = models.Department.objects.all().order_by('name')


class EmployeeDetailView(generic.DetailView):
    model = models.Employee


class EmployeeListView(generic.ListView):
    paginate_by = 20
    model = models.Employee

    def get_queryset(self):
        return super().get_queryset().order_by('surname', 'name').filter(**self.filter_data())

    @cached_property
    def filter_form(self):
        return forms.EmployeeListFilterForm(data=self.request.GET)

    def filter_data(self):
        if self.filter_form.is_valid():
            return self.filter_form.cleaned_data
        return {}

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter_form
        return super().get_context_data(**kwargs)


class AlphabeticalIndex(generic.ListView):
    model = models.Employee
    template_name = 'employees/alphabet.html'
    queryset = models.Employee.objects.order_by('surname').all()

    def get_queryset(self):
        from_char = self.kwargs.get('from') or 'A'
        to_char = self.kwargs.get('to') or 'я'
        return super().get_queryset().filter(Q(surname__range=[from_char, to_char]) | Q(surname__startswith=to_char))

    def get_initial_groups(self):
        from django.db import connection

        cursor = connection.cursor()
        cursor.execute("""
                       SELECT upper(SUBSTR(surname,1,1)),COUNT(*)
                       FROM employees_employee
                       GROUP BY upper(SUBSTR(surname,1,1))
                       ORDER  BY upper(SUBSTR(surname,1,1))
                       """
                       )
        return cursor.fetchall()

    def process_groups(self):
        def merge_groups(a, b):
            result = (a[0][0] + '-' + b[0][-1], a[1] + b[1])
            return result

        groups = self.get_initial_groups()
        while len(groups) > 7:
            min_group = min(groups, key=lambda group: group[1])
            min_group_index = groups.index(min_group)
            try:
                previous_group = groups[min_group_index - 1]
            except IndexError:
                previous_group = None
            try:
                next_group = groups[min_group_index + 1]
            except IndexError:
                next_group = None

            if previous_group is None or (next_group is not None and previous_group[1] > next_group[1]):
                groups[min_group_index] = merge_groups(min_group, next_group)
                groups.remove(next_group)
            else:
                groups[min_group_index] = merge_groups(previous_group, min_group)
                groups.remove(previous_group)
        return groups

    def group_tuples(self):
        groups = self.process_groups()

        def get_group_link(group):
            return reverse('employees:employee:alphabet', kwargs={'from': group[0][0], "to": group[0][-1]})

        return [(group + (get_group_link(group),)) for group in groups]

    def get_context_data(self, **kwargs):

        kwargs['groups'] = self.group_tuples()
        return super().get_context_data(**kwargs)