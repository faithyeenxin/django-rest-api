from rest_framework import serializers
from .models import Project, ProjectEntry
from users_api.serializers import UserSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')
    user = UserSerializer(read_only=True) # this shows entire user detail
    # user = serializers.PrimaryKeyRelatedField(read_only=True) # this shows user id only

    class Meta:
        model = Project
        fields = ('url', 'id', 'project_name', 'user',)

class ProjectEntrySerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:
        model = ProjectEntry
        fields = ('id', 'project', 'email', 'first_name', 'last_name')  # Add other fields here as needed
