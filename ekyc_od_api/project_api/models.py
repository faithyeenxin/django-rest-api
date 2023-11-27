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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_entries')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# {
#     "project": "f1fbd4af-17ce-48b2-9143-d863d6a9a7ee",
#     "email": "example@example.com",
#     "first_name": "John",
#     "last_name": "Doe"
# }