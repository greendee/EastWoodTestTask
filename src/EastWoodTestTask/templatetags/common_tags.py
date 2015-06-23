from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import safe
from django.utils.datastructures import MultiValueDict

register = template.Library()


@register.filter('model_link')
def model_link(model):
    return safe("<a href={url}>{name}</a>".format(name=str(model), url=model.get_url()))


@register.simple_tag
def navactive(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return 'active'
    return ""


@register.simple_tag
def paginator_page_link(request, page_number):
    get = MultiValueDict(request.GET)
    get['page'] = page_number
    return u"{0:s}?{1:s}".format(request.path, "&".join(["%s=%s" % (key, value) for key, value in get.items()]))