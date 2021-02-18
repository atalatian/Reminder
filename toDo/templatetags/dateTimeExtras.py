from django import template
import datetime

register = template.Library()

def subDateTime(taskDateTime):
    currentDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    delta = currentDateTime - taskDateTime
    new_delta = delta - datetime.timedelta(seconds= delta.seconds, microseconds=delta.microseconds)
    return str(new_delta)


register.filter('subDateTime', subDateTime)