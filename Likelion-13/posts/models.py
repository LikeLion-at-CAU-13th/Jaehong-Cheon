from django.db import models
from accounts.models import User
from category.models import Category
# Create your models here.
class BaseModels(models.Model):
    created = models.DateTimeField(auto_now_add=True) # 생성시간
    updated = models.DateTimeField(auto_now=True) # 수정시간

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
 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    

    
    def __str__(self): 
        return self.title
    
    class PostCategory(models.Model):
        post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_category')
        category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')

        class Meta:
            unique_together = ('post', 'category')
        # 게시글-카테고리 중복 방지 !!
        
        def __str__(self):
            return self.category.name