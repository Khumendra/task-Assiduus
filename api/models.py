from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message.split()[0]}"

    # @property
    # def created_by(self):
    #     return self.created_by_set.all()

    class Meta:
        verbose_name_plural = "Message"
