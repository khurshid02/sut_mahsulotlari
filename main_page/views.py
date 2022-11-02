from django.shortcuts import render, redirect
import telebot

from django.http import HttpResponse
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
bot = telebot.TeleBot('5459935331:AAGVWpnqIK_bYMatPGDtqTWS8iPiWZgTJBc')


def home_page(request):
    all_category = models.Category.objects.all()
    all_product = models.Product.objects.all()

    return render(request, 'index.html',
                  {'all_categories': all_category, 'products': all_product })


def product(request, pk):
    product_one = models.Product.objects.get(product_name=pk)
    all_category = models.Category.objects.all()

    return render(request, 'product.html', {'product': product_one, 'all_categories': all_category})


def exact_search(request, pk):
    product = models.Product.objects.get(product_name=pk)
    all_category = models.Category.objects.all()

    return render(request, 'search.html', {'product': product, 'all_category': all_category})


def search(request):
    if request.method == 'POST':
        product = request.POST.get('search_product')

        try:
            models.Product.objects.get(product_name=product)

            return redirect(f'/search/{product}')

        except:
            return redirect('/')


def exact_category(request, pk):
    category = models.Category.objects.get(category_name=pk)
    product = models.Product.objects.filter(product_category = category)

    categories = models.Category.objects.all()

    return render(request, 'category.html', {'product': product, 'category': categories})


def contact(request):
    all_category = models.Category.objects.all()
    return render(request, 'contact.html', { 'all_category': all_category})


def cart_add(request, pk):
    if request.method == 'POST':
        count = models.Product.objects.get(product_name = pk)
        if count.product_count >= int(request.POST.get('pr_count')):
            models.UserCart.objects.create(user_id=request.user.id,
                                           user_product=count,
                                           user_product_quantity=request.POST.get('pr_count')).save()

            return redirect(f'/')

        else:
            return redirect(f'/product/{count.product_name}')


def cart_menu(request):
    id = request.user.id
    cart_menu = models.UserCart.objects.filter(user_id=id)
    all_category = models.Category.objects.all()
    total_sum = 0

    for users in cart_menu:
        total_sum = int(users.user_product_quantity) * float(users.user_product.product_price) + total_sum

    return render(request, 'cart_menu_user.html', {'cart_menu': cart_menu, 'all_categories': all_category, 'sum':total_sum})


def delete(request, pk):
    product = models.Product.objects.get(id = pk)
    models.UserCart.objects.filter(user_id=request.user.id,
                                user_product = product).delete()

    return redirect('/cart')


def shop(request):
    return render(request, 'registration.html')


def buy(request):
    if request.method == 'POST':
        user_id = 1006779184
        total = 0
        user = models.UserCart.objects.filter(user_id = request.user.id)

        text = ' --------- xaridor ----\n'

        text += f'firstname :{request.POST.get("firstname")} \nlastname:{request.POST.get("lastname")}\n' \
                       f'Email :{request.POST.get("email")}\nManzil :{request.POST.get("address")}\n' \
                       f'Tolov turi :{request.POST.get("address_oplata")}\n' \
                f'Telefon nomer :{request.POST.get("number")}\n'

        text += '----- products-----\n'

        for users in user:
            text += f'Tovar :{users.user_product.product_name} \n' \
                       f'Narxi:{users.user_product.product_price}\n' \
                       f'Soni :{users.user_product_quantity}\nZakaz qilingan sanasi :{users.cart_date_add}\n' \
                       f'Xaridor :{users.user_id}\n'
            total = int(users.user_product_quantity) * float(users.user_product.product_price) + total

        for users in user:
            totals = int(users.user_product_quantity) * int(
                                           users.user_product.product_price)
            models.Cart.objects.create(user_id=request.user.id, user=users.user_product.product_name,
                                       count=users.user_product_quantity,
                                       sum=totals).save()
        text += f'summa = {total}\n'

        bot.send_message(user_id, text)
        models.UserCart.objects.filter(user_id=request.user.id).delete()

        return redirect('/cart')


def history(request):
    user_cart = models.Cart.objects.filter(user_id = request.user.id)

    return render(request, 'history.html', {'user_cart': user_cart})
