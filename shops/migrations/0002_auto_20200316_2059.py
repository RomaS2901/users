# Generated by Django 3.0.4 on 2020-03-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='shopmodel',
            name='unique_shop',
        ),
        migrations.AddConstraint(
            model_name='shopmodel',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_shop'),
        ),
    ]
