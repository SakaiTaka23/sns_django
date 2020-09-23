from django.db import models

# Create your models here.


class Post(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content, self.created_at
