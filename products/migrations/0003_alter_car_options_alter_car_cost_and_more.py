# Generated by Django 4.2.6 on 2023-10-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_car_created_at_alter_car_model_of_car'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Авто', 'verbose_name_plural': 'Авто'},
        ),
        migrations.AlterField(
            model_name='car',
            name='cost',
            field=models.PositiveIntegerField(null=True, verbose_name='Укажите цену'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Добавьте описание'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Загрузите фото'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_of_car',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Lexus', 'Lexus'), ('BMW', 'BMW'), ('Subaru', 'Subaru'), ('KIA', 'KIA')], max_length=100, null=True, verbose_name='Выберите марку машины'),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название транспорта'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(null=True, verbose_name='Укажите год выпуска'),
        ),
    ]
