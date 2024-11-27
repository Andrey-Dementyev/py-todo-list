from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
