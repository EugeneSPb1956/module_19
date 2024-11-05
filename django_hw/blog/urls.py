from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.home_page, name='home_page'),
]

# path('posts/', views.get_post_nums, name='get_post_nums'),
