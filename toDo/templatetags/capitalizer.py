from django import template

register = template.Library()

@register.filter
def capitalize(title):
    ans = ""
    words = title.split(" ")
    for word in words:
        ans = ans + " " + word.capitalize()
    return ans.strip()
