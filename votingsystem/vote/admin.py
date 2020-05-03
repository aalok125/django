from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Tag, Question, Answer, GuestUser, GuestUserLog, UserSearchLog, UserVote

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image', 'parent', 'status']
    readonly_fields = ['slug','category_image']

    def category_image(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="150" height="150" />' % (obj.image.url))

    category_image.short_description = 'Image'


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(GuestUser)
admin.site.register(UserVote)
admin.site.register(GuestUserLog)
admin.site.register(UserSearchLog)
