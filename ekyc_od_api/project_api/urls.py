from django.urls import path
from project_api.views import ProjectListCreateView, ProjectDetailView, ProjectEntryListCreateView, ProjectEntryDetailView


urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<uuid:project_id>/entries/', ProjectEntryListCreateView.as_view(), name='project-entry-list-create'),
    path('<uuid:project_id>/entries/<uuid:entry_id>/', ProjectEntryDetailView.as_view(), name='project-entry-detail'),
]
