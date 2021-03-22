from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр книги',
        max_length=30,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание жанра',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        verbose_name='Имя автора',
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name='Информация об авторе',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Название издательства',
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание издательства',
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(
        verbose_name='Серия книг',
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание серии',
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        verbose_name='Возрастная категория',
        max_length=30,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание категории',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(
        verbose_name='Формат книги',
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание формата',
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.name
