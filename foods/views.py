from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


def food_list(request):
    foods = Food.objects.filter(category='kechgi')
    return render(request, 'foods.html', {'foods': foods})


def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    # Ushbu ovqat uchun zarur mahsulotlar (Orders jadvalidan)
    required_orders = Orders.objects.filter(food=food)
    user_products = Products.objects.all()  # Foydalanuvchining uyidagi mahsulotlar

    missing_products = []
    total = 0
    for order in required_orders:
        product = order.products
        needed_quantity = order.quantity_product

        # Foydalanuvchining uyidagi mahsulotni qidirish
        user_product = user_products.filter(name=product.name).first()

        # Agar foydalanuvchi mahsuloti yo‘q yoki yetarli emas bo‘lsa
        if not user_product or user_product.soni < needed_quantity:
            # Yetishmayotgan miqdorni hisoblash
            available_quantity = user_product.soni if user_product else 0
            missing_quantity = needed_quantity - available_quantity
            total += missing_quantity * product.price
            missing_products.append({
                'name': product.name,
                'needed': round(needed_quantity, 2),
                'available': available_quantity,
                'missing': round(missing_quantity, 2),
                'unit': product.unit,
                'sum': round(missing_quantity * product.price, 3)
            })

    return render(request, 'food_detail.html', {
        'food': food,
        'missing_products': missing_products,
        'user_products': user_products,
        "total": total
    })


class ProductListView(View):
    def get(self,request):
        products = Products.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products.html', context)


def salat_list(request):
    foods = Food.objects.filter(category='salat')
    return render(request, 'salatlar.html', {'salats': foods})


def salat_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    # Ushbu ovqat uchun zarur mahsulotlar (Orders jadvalidan)
    required_orders = Orders.objects.filter(food=food)
    user_products = Products.objects.all()  # Foydalanuvchining uyidagi mahsulotlar

    missing_products = []
    total = 0
    for order in required_orders:
        product = order.products
        needed_quantity = order.quantity_product

        # Foydalanuvchining uyidagi mahsulotni qidirish
        user_product = user_products.filter(name=product.name).first()

        # Agar foydalanuvchi mahsuloti yo‘q yoki yetarli emas bo‘lsa
        if not user_product or user_product.soni < needed_quantity:
            # Yetishmayotgan miqdorni hisoblash
            available_quantity = user_product.soni if user_product else 0
            missing_quantity = needed_quantity - available_quantity
            total += missing_quantity * product.price
            missing_products.append({
                'name': product.name,
                'needed': round(needed_quantity, 2),
                'available': available_quantity,
                'missing': round(missing_quantity, 2),
                'unit': product.unit,
                'sum': round(missing_quantity * product.price, 3)
            })

    return render(request, 'food_detail.html', {
        'food': food,
        'missing_products': missing_products,
        'user_products': user_products,
        "total": total
    })


def non_list(request):
    foods = Food.objects.filter(category='nonushta')
    return render(request, 'nonushta.html', {'foods': foods})


def non_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    # Ushbu ovqat uchun zarur mahsulotlar (Orders jadvalidan)
    required_orders = Orders.objects.filter(food=food)
    user_products = Products.objects.all()  # Foydalanuvchining uyidagi mahsulotlar

    missing_products = []
    total = 0
    for order in required_orders:
        product = order.products
        needed_quantity = order.quantity_product

        # Foydalanuvchining uyidagi mahsulotni qidirish
        user_product = user_products.filter(name=product.name).first()

        # Agar foydalanuvchi mahsuloti yo‘q yoki yetarli emas bo‘lsa
        if not user_product or user_product.soni < needed_quantity:
            # Yetishmayotgan miqdorni hisoblash
            available_quantity = user_product.soni if user_product else 0
            missing_quantity = needed_quantity - available_quantity
            total += missing_quantity * product.price
            missing_products.append({
                'name': product.name,
                'needed': round(needed_quantity, 2),
                'available': available_quantity,
                'missing': round(missing_quantity, 2),
                'unit': product.unit,
                'sum': round(missing_quantity * product.price, 3)
            })

    return render(request, 'non_detail.html', {
        'food': food,
        'missing_products': missing_products,
        'user_products': user_products,
        "total": total
    })


def tush_list(request):
    foods = Food.objects.filter(category='tushlik')
    return render(request, 'tushlik.html', {'foods': foods})


def tush_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    # Ushbu ovqat uchun zarur mahsulotlar (Orders jadvalidan)
    required_orders = Orders.objects.filter(food=food)
    user_products = Products.objects.all()  # Foydalanuvchining uyidagi mahsulotlar

    missing_products = []
    total = 0
    for order in required_orders:
        product = order.products
        needed_quantity = order.quantity_product

        # Foydalanuvchining uyidagi mahsulotni qidirish
        user_product = user_products.filter(name=product.name).first()

        # Agar foydalanuvchi mahsuloti yo‘q yoki yetarli emas bo‘lsa
        if not user_product or user_product.soni < needed_quantity:
            # Yetishmayotgan miqdorni hisoblash
            available_quantity = user_product.soni if user_product else 0
            missing_quantity = needed_quantity - available_quantity
            total += missing_quantity * product.price
            missing_products.append({
                'name': product.name,
                'needed': round(needed_quantity, 2),
                'available': available_quantity,
                'missing': round(missing_quantity, 2),
                'unit': product.unit,
                'sum': round(missing_quantity * product.price, 3)
            })

    return render(request, 'tush_detail.html', {
        'food': food,
        'missing_products': missing_products,
        'user_products': user_products,
        "total": total
    })


def drinks(request):

    drinks = Drinks.objects.all()
    return render(request, 'ichimliklar.html', {'drinks': drinks})
