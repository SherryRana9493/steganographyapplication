# Generated by Django 5.0.2 on 2024-02-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageUpload', '0002_alter_imagemodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergeImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=100)),
                ('secret_image', models.ImageField(default=None, max_length=250, null=True, upload_to='mergeimages/')),
                ('cover', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(default=None, max_length=250, null=True, upload_to='mergeimages/')),
            ],
        ),
    ]