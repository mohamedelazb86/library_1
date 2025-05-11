from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post,Review,Category

class PostAdmin(SummernoteModelAdmin):
    list_display=['title','publish_date','draft']
    search_fields=['ttile','content']
    list_filter=['draft']
    summernote_fields=['content',]

admin.site.register(Post,PostAdmin)
admin.site.register(Review)
admin.site.register(Category)
