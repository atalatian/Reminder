from django import forms
from .models import Task
from .models import Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description",
                  "category", "priority", "schedule"]

    title = forms.CharField(max_length=255, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="description")
    priority = forms.IntegerField(label="priority")
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
    )
    schedule = forms.DateTimeField(input_formats="%Y-%m-%d %H:%M",
                                   label="schedule",
                                   widget=forms.DateTimeInput(
                                       attrs={'placeholder': 'Example: 2006-10-25 14:30'}))
