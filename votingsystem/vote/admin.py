from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Tag, Question, Answer, GuestUser, GuestUserLog, UserSearchLog, UserVote

# Register your models here.

admin.site.site_header = "Vote Anything"
admin.site.site_title = "Vote Anything"
admin.site.index_title = "Welcome to Vote Anything Admin Panel"



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image', 'parent', 'status']
    readonly_fields = ['slug','category_image']

    def category_image(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="150" height="150" />' % (obj.image.url))

    category_image.short_description = 'Image'




class AnswerInline(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'question_image', 'question_tag', 'category', 'status']
    readonly_fields = ['slug', 'question_image', 'question_tag']

    def question_tag(self, obj):
        if obj.tags:
            return ", ".join([
                child.title for child in obj.tags.all()
            ])

    question_tag.short_description = "Tags"

    def question_image(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="150" height="150" />' % (obj.image.url))

    question_image.short_description = 'Image'

    inlines = [AnswerInline]





admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
admin.site.register(GuestUser)
admin.site.register(UserVote)
admin.site.register(GuestUserLog)
admin.site.register(UserSearchLog)
