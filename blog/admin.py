from django.contrib import admin
from blog.models import *

# Register your models here.


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 2


class PostAdmin(admin.ModelAdmin):
    list_display_links = ['id']
    list_display = ['id', 'title', 'description', 'category', 'created', 'updated']
    list_editable = ['title', 'category']
    search_fields = ['title', 'description']
    list_filter = ['created', 'category']
    readonly_fields = ['created', 'updated']
    inlines = [ReviewInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)