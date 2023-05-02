from django.contrib import admin

# Register your models here.
from .models import Profile
from django.utils.safestring import mark_safe

@admin.register(Profile)
class CommentAdmin(admin.ModelAdmin):
    
    list_display =['id', 'user', 'address', 'zipcode']
    list_display_links = ['id', 'user']
    search_fields = ['user', 'zipcode']
    list_filter = []