# Generated by Django 4.2.13 on 2024-07-12 10:13

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_story_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]