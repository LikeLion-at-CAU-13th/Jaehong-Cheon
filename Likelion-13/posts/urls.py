from django.urls import path
from posts.views import *

urlpatterns = [
		#path("", hello_world, name="hello_world"),
    #path("page", index, name="my-page"),
    #path('<int:id>', get_post_detail),
    
    path('', PostList.as_view()),
    path('<int:post_id>/', PostDetail.as_view()) # Post ?? ??
]