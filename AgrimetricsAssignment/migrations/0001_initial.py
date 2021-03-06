# Generated by Django 3.1.4 on 2021-12-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateSandwichOrder',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('base', models.CharField(max_length=50)),
                ('meat_one', models.CharField(max_length=50)),
                ('meat_two', models.CharField(max_length=50)),
                ('cheese', models.CharField(max_length=50)),
                ('sauce', models.CharField(max_length=50)),
                ('salad', models.BooleanField(default=True)),
                ('extra', models.CharField(max_length=150)),
            ],
        ),
    ]
