# Generated by Django 3.1.4 on 2021-12-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgrimetricsAssignment', '0003_createsandwichorder_table_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createsandwichorder',
            name='table_number',
        ),
        migrations.AddField(
            model_name='createsandwichorder',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]