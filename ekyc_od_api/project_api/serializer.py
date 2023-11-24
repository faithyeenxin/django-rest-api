from rest_framework import serializers
from .models import Project
from users_api.serializers import UserSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')
    user = UserSerializer()

    class Meta:
        model = Project
        fields = ('url', 'id', 'project_name', 'user')
