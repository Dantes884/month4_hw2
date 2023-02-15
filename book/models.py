from django.db import models

class Book(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('ROMAN', 'ROMAN'),
        ('DETECTIVE', 'DETECTIVE'),
        ('ADVENTURE', 'ADVENTURE'),
    )


    title = models.CharField('Название книги', max_length=100)
    author = models.TextField('Автор книги')
    description = models.TextField('Описание книги')
    image = models.ImageField('Картинка', upload_to='')
    quantity = models.PositiveIntegerField('Количество страниц')
    genre = models.CharField('Жанр', max_length=100, choices=GENRE)
    link = models.URLField('Ссылка на книгу')
    price = models.PositiveIntegerField('Цена')
    mass = models.PositiveIntegerField('Масса книги в граммах')
    age_limit = models.PositiveIntegerField('Возрастное ограничение')


    def __str__(self):
        return self.title