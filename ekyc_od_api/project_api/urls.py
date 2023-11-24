from django.urls import path
from project_api.views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
