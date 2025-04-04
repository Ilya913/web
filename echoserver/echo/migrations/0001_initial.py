# Generated by Django 5.1.7 on 2025-03-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.AutoField(primary_key=True, serialize=False)),
                ('name_book', models.CharField(max_length=64)),
                ('author_book', models.CharField(max_length=64)),
                ('price_book', models.DecimalField(decimal_places=2, max_digits=10)),
                ('genre_book', models.CharField(max_length=64)),
                ('publication_year_book', models.IntegerField()),
                ('publisher_book', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
