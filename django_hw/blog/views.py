from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog
# from django import forms
# from django.forms import widgets
# from .forms import UserRegister

# class UserRegister(forms.Form):
# #     select_posts = forms.Select
#     CHOICES = ((3,), (4,), (5,), (6,), (6,), (7,), (8,), (9,), (10,))
#     choice_field = forms.ChoiceField(widget=forms.Select, choices=CHOICES)


# Create your views here.
# def home_page(request):
#     blogs = Blog.objects.all()
#     paginator = Paginator(blogs, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj, 'range': range(3, 11), 'selection': 3}
#     return render(request, 'posts/home_page.html', context)


# def get_post_nums(request):
#     # print('зашли в get_post_nums')
#     if request.method == 'POST':
#         # print('request.method == POST')
#         # val1 = request.POST.get('name')
#         val = request.POST.get('select')
#         print('Выбор =', val)
#         blogs = Blog.objects.all()
#         paginator = Paginator(blogs, val)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context = {'page_obj': page_obj, 'range': range(3, 11), 'selection': val}
#         return render(request, 'posts/home_page.html', context)

val = 3

def home_page(request):
    global val
    if request.method == 'POST':
        val = request.POST.get('select')
        print('Выбор =', val)
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, val)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'range': range(3, 11), 'selection': int(val),}
    return render(request, 'posts/home_page.html', context)

