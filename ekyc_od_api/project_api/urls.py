from django.urls import path
from project_api.views import ProjectListCreateView, ProjectDetailView, ProjectEntryListCreateView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    # path('<uuid:project_id>/project-entries/', ProjectEntryListCreateView.as_view(), name='project-entry-list-create'),
    # path('project-entries/', ProjectEntryListCreateView.as_view(), name='project-entry-list-create'),
    # path('project-entries/<uuid:pk>/', ProjectDetailView.as_view(), name='project-entry-detail'),
]
