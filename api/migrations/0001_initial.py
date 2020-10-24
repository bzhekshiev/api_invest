# Generated by Django 3.1.2 on 2020-10-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('doc_num', models.CharField(max_length=20, verbose_name='Серия и номер')),
                ('birth_place', models.CharField(max_length=100, verbose_name='Место рождения')),
                ('issue_date', models.DateField(verbose_name='Дата выдачи')),
                ('division_code', models.CharField(max_length=10, verbose_name='Код подразделения')),
                ('issue_by', models.CharField(max_length=200, verbose_name='Кем выдан')),
                ('reg_address', models.CharField(max_length=200, verbose_name='Адрес регистрации')),
                ('doc_first_page', models.FileField(upload_to=None, verbose_name='Разворот с фото')),
                ('doc_second_page', models.FileField(upload_to=None, verbose_name='Разворот с регистрацией')),
            ],
        ),
    ]
