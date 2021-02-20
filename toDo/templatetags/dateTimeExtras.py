from django import template
import datetime
import pytz

register = template.Library()


@register.simple_tag
def subDateTime(taskDateTime):
    currentDateTime = datetime.datetime.now()
    currentDateTime = currentDateTime.replace(tzinfo=None)
    taskDateTime = taskDateTime.replace(tzinfo=None)
    delta = taskDateTime - currentDateTime
    new_delta = delta - datetime.timedelta(microseconds=delta.microseconds)
    return str(new_delta)
