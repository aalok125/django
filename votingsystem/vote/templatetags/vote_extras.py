from django import template

register = template.Library()

#helpers to return object at specific index of list

@register.filter
def get_index_title(list, index):
    return list[index].title

@register.filter
def get_index_image(list, index):
    return list[index].image.url

@register.filter
def get_index_votes(list, index):
    return list[index].votes

@register.filter
def start_from_4th(list):
    return list[3:]