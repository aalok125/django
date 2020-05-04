from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from votingsystem.utils import unique_slug_generator

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/images/categories', blank=True, null=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    parent = models.ForeignKey(to='Category', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def children(self):
        return Category.objects.filter(parent = self.id)


class Tag(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length=225, unique=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/images/categories', blank=True, null=True)
    category = models.ForeignKey(to='Category', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='uploads/images/categories', blank=True, null=True)
    question = models.ForeignKey(to='Question', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class GuestUser(models.Model):
    UserStatus = ('Active', 'Active'), ('Inactive', 'Inactive'), ('Block','Block'), ('Suspended', 'Suspended')

    ipaddress = models.GenericIPAddressField(unique=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, choices=UserStatus)

    def __str__(self):
        return self.ipaddress


class UserVote(models.Model):
    guest_user = models.ForeignKey(to='GuestUser', on_delete=models.CASCADE)
    question = models.ForeignKey(to='Question', on_delete=models.CASCADE)
    answer = models.ForeignKey(to='Answer', on_delete=models.CASCADE)

    def __str__(self):
        return self.guest_user


class GuestUserLog(models.Model):
    guest_user = models.ForeignKey(to='GuestUser', on_delete=models.CASCADE)
    question = models.ForeignKey(to='Question', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.guest_user






class UserSearchLog(models.Model):
    guest_user = models.ForeignKey(to='GuestUser', on_delete=models.CASCADE)
    search_text = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.guest_user



def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_reciver, sender=Category)
pre_save.connect(pre_save_post_reciver, sender=Question)
pre_save.connect(pre_save_post_reciver, sender=Tag)







