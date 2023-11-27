from rest_framework import serializers
from .models import Project, ProjectEntry
from users_api.serializers import UserSerializer

class ProjectEntrySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-entry-list-create')
    class Meta:
        model = ProjectEntry
        fields = ('url', 'id', 'email', 'first_name', 'last_name')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')
    user = UserSerializer(read_only=True) # this shows entire user detail
    project_entries = ProjectEntrySerializer(many=True, read_only=True) # this shows entire user detail
    # user = serializers.PrimaryKeyRelatedField(read_only=True) # this shows user id only

    class Meta:
        model = Project
        fields = ('url', 'id', 'project_name', 'user','project_entries')

