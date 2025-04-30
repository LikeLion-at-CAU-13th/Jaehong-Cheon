from django.contrib import admin
from .models import Post
# Register your models here.
from django.contrib import admin
from .models import Post, PostCategory

class PostCategoryInline(admin.TabularInline):  # �Ǵ� StackedInline
    model = PostCategory
    extra = 1  # �⺻ �Է� ĭ 1��
    verbose_name = "category"
    verbose_name_plural = "categoryList"

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline]

admin.site.register(Post, PostAdmin)