from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("task/add/", views.TaskCreateView.as_view(), name="add_task"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="update_task"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="delete_task"),
    path(
        "task/<int:pk>/toggle/",
        views.TaskToggleView.as_view(),
        name="toggle_task_status",
    ),
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tag/add/", views.TagCreateView.as_view(), name="add_tag"),
    path("tag/<int:pk>/update/", views.TagUpdateView.as_view(), name="update_tag"),
    path("tag/<int:pk>/delete/", views.TagDeleteView.as_view(), name="delete_tag"),
]

app_name = "task_tag"
