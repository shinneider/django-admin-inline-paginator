import urllib.parse

from django import template

register = template.Library()


@register.simple_tag
def modify_pagination_path(full_path: str, key: str, value: str) -> str:
    get_params = full_path
    if get_params.find('?') > -1:
        get_params = get_params[get_params.find('?')+1:]
    if get_params.find('#') > -1:
        get_params = get_params[:get_params.find('#')]

    params = urllib.parse.parse_qs(get_params)
    params[key] = [str(value)]
    return urllib.parse.urlencode(params, doseq=True)
