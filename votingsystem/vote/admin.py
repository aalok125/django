from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Tag, Question, Answer, GuestUser, GuestUserLog, UserSearchLog, UserVote

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image', 'parent', 'status']
    readonly_fields = ['category_image']

    # image show in admin list
    def category_image(self, obj):
        if obj.id:
            return mark_safe('<img src="%s" height="150">' % obj.image.url)
        return ''

    category_image.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(GuestUser)
admin.site.register(UserVote)
admin.site.register(GuestUserLog)
admin.site.register(UserSearchLog)
