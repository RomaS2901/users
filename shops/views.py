from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from .models import ShopModel
from .forms import UpdateShopForm, CreateShopForm


@user_passes_test(lambda u: u.is_superuser)
def shops(request):
    return render(request, 'shops/shops.html', context={
        'shops': ShopModel.objects.all(),
        'update_shop_form': UpdateShopForm(),
        'create_shop_form': CreateShopForm()
    })


def shops_create(request):
    create_form = CreateShopForm(request.POST)
    if create_form.is_valid():
        create_form.save()
        return redirect('shops:list')
    return render(request, 'shops/shops.html', context={
        'shops': ShopModel.objects.all(),
        'update_shop_form': UpdateShopForm(),
        'create_shop_form': create_form
    })


def shops_update(request):
    shop = get_object_or_404(ShopModel, pk=request.POST.get('shop_number'))
    update_form = UpdateShopForm(request.POST, instance=shop)
    if update_form.is_valid():
        update_form.save()
        return redirect('shops:list')
    return render(request, 'shops/shops.html', context={
        'shops': ShopModel.objects.all(),
        'update_shop_form': update_form,
        'create_shop_form': CreateShopForm()
    })


def shops_delete(request, pk):
    shop = get_object_or_404(ShopModel, pk=pk)
    shop.delete()
    return redirect('shops:list')