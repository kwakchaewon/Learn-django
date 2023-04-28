from django.contrib import admin

# Register your models here.
from .models import Post
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    # 원하는 필드
    list_display = ['id', 'photo_tag', 'message','created_at', 'updated_at','is_public','messeage_length']
    
    # 링크 설정
    list_display_links = ['message']
    
    # 검색 필드
    search_fields=['message']
    
    # 검색 필터
    list_filter=['is_public']
    
    # 사용자 정의 필드
    def messeage_length(self, post):
        return f'{len(post.message)} 글자'
    
    # 사진 미리보기
    def photo_tag(self, post):
        if post.photo:
            return mark_safe( f'<img src="{post.photo.url}" style = "width:75px;" />')
        return None