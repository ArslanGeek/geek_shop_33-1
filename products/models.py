from django.db import models

class Car(models.Model):

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Авто'

    CAR_MODEL = (
        ('Toyota', 'Toyota'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Lexus', 'Lexus'),
        ('BMW', 'BMW'),
        ('Subaru', 'Subaru'),
        ('KIA', 'KIA'),
    )


    title = models.CharField(max_length=100, null=True, verbose_name='Название транспорта')
    image = models.ImageField(upload_to='', null=True, verbose_name='Загрузите фото')
    description = models.TextField(blank=True, null=True, verbose_name='Добавьте описание')
    model_of_car = models.CharField(max_length=100, choices=CAR_MODEL, null=True, verbose_name='Выберите марку машины')
    cost = models.PositiveIntegerField(null=True, verbose_name='Укажите цену')
    year = models.PositiveIntegerField(null=True, verbose_name='Укажите год выпуска')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Марка: {self.model_of_car}\n' \
               f'Цена: {self.cost}$'