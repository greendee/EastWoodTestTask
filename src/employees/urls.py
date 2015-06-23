from . import views
from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',
    url(r'^employee/', include(patterns(
        '',
        url(r'^list/$', views.EmployeeListView.as_view(), name='list'),
        url(r'^detail/(?P<pk>\d+)/$', views.EmployeeDetailView.as_view(), name='detail'),
        url(r'^alphabet(?:/(?P<from>\w+)/(?P<to>\w+))?/$', views.AlphabeticalIndex.as_view(), name='alphabet'),
    ), namespace='employee')),
    url(r'^department/', include(patterns(
        '',
        url(r'^list/$', views.DepartmentListView.as_view(), name='list'),
        url(r'^detail/(?P<pk>\d+)/$', views.DepartmentDetailView.as_view(), name='detail'),
    ), namespace='department')),
)

