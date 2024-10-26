from django.shortcuts import render
# from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game


info = {'user': ''}


# Create your views here.
def platform_view(request):
    return render(request, 'first_task/platform.html')


def games_view(request):
    games = list(Game.objects.all())
    print(games)
    return render(request, 'first_task/games.html', context={'games': games})


orders = [
    ['Заказ 1', 10, 'б/у'],
    ['Заказ 2', 17800, 'отличное'],
    ['Заказ 3', 310, 'хорошее'],
    ['Заказ 4', 100, 'хорошее'],
]
orders_cnt = len(orders)
# orders_cnt = 0    #  <-- отладка. Для проверки отсутствия заказов
total = sum([order[1] for order in orders])


def cart_view(request):
    return render(request, 'first_task/cart.html',
                  context={'orders': orders, 'total': total, 'orders_cnt': orders_cnt})


def menu(request):
    return render(request, 'first_task/menu.html')

# =============================


def sign_up_by_django(request):
    if request.method == 'POST':

        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            buyer = Buyer.objects.filter(name=username)

            # проверка наличия пользователя
            if password == repeat_password and age >= 18 and not buyer:
                Buyer.objects.create(name=username, age=age)
                return render(request, 'first_task/registration_page.html', {'user': f'Приветствуем, {username}!'})
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'first_task/registration_page.html', context=info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'first_task/registration_page.html', context=info)
            elif buyer:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'first_task/registration_page.html', context=info)
            else:
                print('Неизвестная ошибка')
                info['error'] = 'Неизвестная ошибка'
                return render(request, 'first_task/registration_page.html', context=info)
    else:
        return render(request, 'first_task/registration_page.html', context=info)


def sign_up_by_html(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # проверка наличия пользователя
        buyer = Buyer.objects.filter(name=username)
        if password == repeat_password and age >= 18 and not buyer:
            Buyer.objects.create(name=username, age=age)
            return render(request, 'first_task/registration_page.html', {'user': f'Приветствуем, {username}!'})
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'first_task/registration_page.html', context=info)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'first_task/registration_page.html', context=info)
        elif buyer:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'first_task/registration_page.html', context=info)
        else:
            print('Неизвестная ошибка')
    else:
        return render(request, 'first_task/registration_page.html', {'user': ''})
