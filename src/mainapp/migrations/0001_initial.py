# Generated by Django 3.1.5 on 2021-03-22 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название книги')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Цена (BYN)')),
                ('year', models.SmallIntegerField(default=1900, verbose_name='Год издания')),
                ('num_pages', models.SmallIntegerField(default=0, verbose_name='Количество страниц')),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, verbose_name='ISBN')),
                ('weight', models.SmallIntegerField(default=0, verbose_name='Вес (гр)')),
                ('qty', models.SmallIntegerField(default=0, verbose_name='Наличие (шт)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступен для заказа')),
                ('rating', models.FloatField(default=0.0, verbose_name='Рейтинг')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('authors', models.ManyToManyField(blank=True, to='references.Author', verbose_name='Авторы книги')),
                ('book_format', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='references.format')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='references.category')),
                ('genres', models.ManyToManyField(blank=True, to='references.Genre', verbose_name='Жанры')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='references.publisher')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='references.series')),
            ],
        ),
    ]