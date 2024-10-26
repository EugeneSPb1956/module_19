from django.urls import path
from . import views

app_name = 'task1'

urlpatterns = [
    # post views
    path('platform/', views.platform_view, name='platform_view'),
    path('games/', views.games_view, name='games_view'),
    path('cart/', views.cart_view, name='cart_view'),
    path('menu/', views.menu),
    path('', views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
]

