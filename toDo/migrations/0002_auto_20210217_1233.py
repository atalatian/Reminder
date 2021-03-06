# Generated by Django 3.1.6 on 2021-02-17 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default='uncategorized', on_delete=django.db.models.deletion.SET_DEFAULT, to='toDo.category'),
        ),
    ]
