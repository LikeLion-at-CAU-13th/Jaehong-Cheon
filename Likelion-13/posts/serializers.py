from config.custom_api_exceptions import PostConflictException
from rest_framework import serializers
from .models import Post, Image
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate(self, data):
        user = data.get('user')  # 이미 DRF가 User 객체로 변환해줌

        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = now.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        required_fields = ['title', 'content', 'status', 'user']
        for field in required_fields:
          raw_value = self.initial_data.get(field)
          if raw_value in [None, '', []]:
            raise serializers.ValidationError({field: f"{field} 필드는 필수입니다."})

        # 하루에 한 번만 작성 가능 (같은 user, 같은 날짜)
        # if Post.objects.filter(user=user, created__range=(today_start, today_end)).exists():
        #     raise ValidationError({
        #         "user": "해당 유저는 오늘 이미 게시글을 작성했습니다."
        #     })

        # 같은 제목 중복 방지 (같은 user 기준)
        if Post.objects.filter(title=data['title'], user=user).exists():
            raise PostConflictException({
                "title": f"A post with the title '{data['title']}' already exists for this user."
            })
        


        return data

    class Meta:
        model = Post
        fields = '__all__'




class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        fields = ['image']