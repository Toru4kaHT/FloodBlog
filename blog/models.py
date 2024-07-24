from django.contrib.auth.models import User
from django.db import models


class ModelBlog(models.Model):
    title = models.CharField(max_length=25, null=False)
    content = models.TextField(null=False)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.pub_date}'

# Create your models here.
