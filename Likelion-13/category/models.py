from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 카테고리 이름
    

    def __str__(self):
        return self.name
