from django.contrib.auth.models import User
from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
    
class ProjectEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='entries', on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"{self.project.project_name} - Entry {self.id}"
