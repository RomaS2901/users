from django import forms
from .models import ShopModel


class CreateShopForm(forms.ModelForm):

    class Meta:
        model = ShopModel
        fields = '__all__'


class UpdateShopForm(forms.ModelForm):
    """ For now Update and Create forms are the same. But we should follow single responsibility rule and
            keep them separate for future changes... """
    class Meta:
        model = ShopModel
        fields = ('user', 'name', 'shop_number')
