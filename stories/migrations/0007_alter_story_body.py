# Generated by Django 4.2.13 on 2024-07-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_alter_story_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='body',
            field=models.TextField(default='this is where you add your story'),
        ),
    ]