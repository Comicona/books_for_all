# Generated by Django 3.1.5 on 2021-03-22 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksincart',
            name='book_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_cards', to='mainapp.bookcard', verbose_name='Книга'),
        ),
        migrations.AddField(
            model_name='booksincart',
            name='customer_cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books_in_cart', to='cart.customercart', verbose_name='Корзина товаров'),
        ),
    ]
