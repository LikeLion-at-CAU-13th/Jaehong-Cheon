from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 카테고리 이름
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    def __str__(self):
        return self.name
