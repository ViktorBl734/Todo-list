from django.urls import path
from django.views import View


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("create_task/", TaskCreateView.as_view(), name="task-create"),
    path("update_task/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete_task/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("toggle_task/<int:pk>/", toggle_task_status, name="task-toggle"),
]
