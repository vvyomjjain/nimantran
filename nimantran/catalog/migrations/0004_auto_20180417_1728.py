# Generated by Django 2.0.1 on 2018-04-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180403_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cateory',
            field=models.ManyToManyField(help_text='Select a category for this event', to='catalog.Category'),
        ),
    ]
