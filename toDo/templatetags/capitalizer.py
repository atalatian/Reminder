from django import template

register = template.Library()

@register.filter
def capitalize(title):
    ans = ""
    words = title.split(" ")
    for word in words:
        ans = word.capitalize() + " " + ans
    return ans.strip()
