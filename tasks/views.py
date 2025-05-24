from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TagListView(ListView):
    model = Tag


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")


def toggle_task_status(request, task_id):
    task = get_object_or_404(id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("task-list")
