from django.contrib import admin
from .models import Category, Tag, Question, Answer, GuestUser, GuestUserLog, UserSearchLog, UserVote

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'parent', 'status']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(GuestUser)
admin.site.register(UserVote)
admin.site.register(GuestUserLog)
admin.site.register(UserSearchLog)
