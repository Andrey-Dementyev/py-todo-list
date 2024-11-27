from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Task, Tag
from .forms import TaskForm, TagForm


def home(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("done", "-creation_time")
    return render(request, "task_tag/home.html", {"tasks": tasks})


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_tag/task_form.html"
    success_url = reverse_lazy("task_tag:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_tag/task_form.html"
    success_url = reverse_lazy("task_tag:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_tag/task_confirm_delete.html"
    success_url = reverse_lazy("task_tag:home")


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save(update_fields=["done"])
        return redirect("task_tag:home")


class TagListView(ListView):
    model = Tag
    template_name = "task_tag/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "task_tag/tag_form.html"
    success_url = reverse_lazy("task_tag:tag_list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "task_tag/tag_form.html"
    success_url = reverse_lazy("task_tag:tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "task_tag/tag_confirm_delete.html"
    success_url = reverse_lazy("task_tag:tag_list")
