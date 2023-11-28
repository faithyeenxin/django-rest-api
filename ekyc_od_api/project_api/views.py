from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, ProjectEntry
from .serializer import ProjectSerializer, ProjectEntrySerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from ekyc_od_api.custom_permissions import IsSuperUserOrStaffUser
from rest_framework.generics import get_object_or_404
class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
         if self.request.method == 'POST':
            return [IsSuperUserOrStaffUser()]
         return super().get_permissions()

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        # if project.user == request.user:
        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk):
        project = self.get_object(pk)
        if project.user == request.user:
            serializer = ProjectSerializer(project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        project = self.get_object(pk)
        if project.user == request.user:
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

class ProjectEntryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsSuperUserOrStaffUser()]
        return super().get_permissions()
    
    def get_project(self, project_id):
        try:
            return Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, project_id):
        project = self.get_project(project_id)
        entries = project.entries.all()
        serializer = ProjectEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        request.data['project'] = project.id  # Include project ID in request data
        serializer = ProjectEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class ProjectEntryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, project_id, entry_id):
        try:
            project = Project.objects.get(pk=project_id)
            return project.entries.get(pk=entry_id)
        except (Project.DoesNotExist, ProjectEntry.DoesNotExist):
            raise Http404

    def get(self, request, project_id, entry_id):
        entry = self.get_object(project_id, entry_id)
        serializer = ProjectEntrySerializer(entry)
        return Response(serializer.data)

    def patch(self, request, project_id, entry_id):
        entry = self.get_object(project_id, entry_id)
        serializer = ProjectEntrySerializer(entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, entry_id):
        entry = self.get_object(project_id, entry_id)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
