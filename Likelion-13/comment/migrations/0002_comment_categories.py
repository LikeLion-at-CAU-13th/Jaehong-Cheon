# Generated by Django 5.1.7 on 2025-03-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='category.category'),
        ),
    ]
