# Generated by Django 5.1.1 on 2024-09-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=150)),
                ('age', models.IntegerField()),
                ('books', models.ManyToManyField(to='books.books')),
            ],
        ),
    ]
