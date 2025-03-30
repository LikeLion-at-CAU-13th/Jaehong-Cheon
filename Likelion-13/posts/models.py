from django.db import models
from accounts.models import User
# Create your models here.
class BaseModels(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModels):

    CHOICES = (
        ('STORED', '보관관'),
        ('PUBLISHED', '발행'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    status = models.CharField(max_length=15, choices=CHOICES, default='STORED')
    created = models.DateTimeField(auto_now_add=True) # ��ü�� ������ �� ��¥�� �ð� ����
    updated = models.DateTimeField(auto_now=True)  # ��ü�� ������ �� ��¥�� �ð� ����
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    
    def __str__(self): # ǥ�� ���̽� Ŭ���� �޼���, �����? ���� �� �ִ� ���ڿ��� ��ȯ�ϵ��� ��
        return self.title