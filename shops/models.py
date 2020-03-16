from django.db import models
from django.conf import settings
from django.db.models.constraints import UniqueConstraint


class ShopModel(models.Model):

    shop_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'shops'
        constraints = [
            UniqueConstraint(fields=['name', 'user'], name='unique_shop')
        ]
