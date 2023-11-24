from django.urls import path
from project_api.views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
