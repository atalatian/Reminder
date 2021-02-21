from django import template

register = template.Library()

@register.filter
def process(title, url):
    for i in title:
        if i == " ":
            title = title.replace(" ", "_")
    return url + title
