from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=5) # �ۼ��� �̸� ����
    content = models.TextField() # ��� ���� ����
    created_at = models.DateTimeField(auto_now_add=True)  # �ۼ� �ð�
    updated_at = models.DateTimeField(auto_now=True)      # ���� �ð�
    
    def __str__(self):
        return f"{self.author_name} - {self.content[:20]}"
