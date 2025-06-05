from django.shortcuts import render
from django.http import JsonResponse # �߰� 
from django.shortcuts import get_object_or_404 # �߰�
from django.views.decorators.http import require_http_methods # �߰�
from .models import * # �߰�
import json
from comment.models import Comment
from .serializers import PostSerializer
# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsAuthor, IsValidTime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.files.storage import default_storage  
from .serializers import ImageSerializer
from django.conf import settings
import boto3

class PostList(APIView):
    permission_classes = [IsAuthor, IsValidTime]
    @swagger_auto_schema(
        operation_summary="게시글 생성",
        operation_description="새로운 게시글을 생성합니다.",
        request_body=PostSerializer,
        responses={201: PostSerializer, 400: "잘못된 요청"}
    )
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
            operation_summary= "게시글 목록 조회",
            operation_description= "모든 게시글을 조회합니다.",
            responses={200: PostSerializer(many=True)}
    )
    def get(slef, request, format=None):
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor, IsValidTime]

    @swagger_auto_schema(
            operation_summary="특정 게시글 조회",
            operation_description="특정 게시글을 조회합니다.",
            request_body= PostSerializer,
            responses={}
    )
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ImageUploadView(APIView):
    def post(self, request):
        if 'image' not in request.FILES:
            return Response({"error": "No image file"}, status=status.HTTP_400_BAD_REQUEST)

        image_file = request.FILES['image']

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )

        # S3에 파일 저장
        file_path = f"uploads/{image_file.name}"
        # S3에 파일 업로드
        try:
            s3_client.put_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=file_path,
                Body=image_file.read(),
                ContentType=image_file.content_type,
            )
        except Exception as e:
            return Response({"error": f"S3 Upload Failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 업로드된 파일의 URL 생성
        image_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{file_path}"

        # DB에 저장
        image_instance = Image.objects.create(image_url=image_url)
        serializer = ImageSerializer(image_instance)


        return Response(serializer.data, status=status.HTTP_201_CREATED)