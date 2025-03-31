from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=5) # 작성자 이름 저장
    content = models.TextField() # 댓글 내용 저장
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)      # 수정 시간
    
    def __str__(self):
        return f"{self.author_name} - {self.content[:20]}"
