# Generated by Django 4.2.4 on 2023-09-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True, verbose_name='nombre clave')),
                ('name', models.CharField(max_length=50, verbose_name='red social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='enlace')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modificacion')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['-created'],
            },
        ),
    ]