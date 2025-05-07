from django.urls import path
from posts.views import *
from comment.views import *

urlpatterns = [
    path('post/<int:post_id>/', Comment_list.as_view()) # Post ?? ??
]