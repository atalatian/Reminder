# Generated by Django 3.1.6 on 2021-02-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0004_auto_20210217_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(default='uncategorized', to='toDo.Category'),
        ),
    ]
