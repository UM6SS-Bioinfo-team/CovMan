# Generated by Django 4.1 on 2022-08-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='identifiant',
            field=models.CharField(default='admin1', max_length=100, unique=True, verbose_name='Identifier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='institut',
            field=models.CharField(max_length=250, verbose_name='Institut'),
        ),
    ]