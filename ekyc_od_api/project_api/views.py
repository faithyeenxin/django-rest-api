from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializer import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .custom_permissions import IsSuperUserOrStaffUser
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
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        if project.user == request.user:
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
