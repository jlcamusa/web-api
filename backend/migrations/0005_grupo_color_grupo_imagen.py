# Generated by Django 4.1 on 2023-07-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_resultado_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='color',
            field=models.CharField(default='null', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='imagen',
            field=models.CharField(default='null', max_length=400),
            preserve_default=False,
        ),
    ]
