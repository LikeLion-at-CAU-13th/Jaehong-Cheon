from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
  def validate_content(self, value):
        if len(value.strip()) < 15:
            raise serializers.ValidationError("댓글을 15자 이상 입력해주세요 ㅎㅎ")
        return value

  class Meta:
		# 어떤 모델을 시리얼라이즈할 건지
    model = Comment
		# 모델에서 어떤 필드를 가져올지
		# 전부 가져오고 싶을 때
    fields = "__all__"