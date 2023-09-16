from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text_content = models.TextField(max_length=5000)
    def __str__(self):
        return self.user.username


class JobRole(models.Model):
    resume = models.ForeignKey(Resume, related_name="job_roles", on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]  # this ensures roles are ordered by the order they were added

    def __str__(self):
        return self.role