# Generated by Django 3.0.8 on 2020-07-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_mix_bgcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix',
            name='bgcolor',
            field=models.CharField(default='#9cc754', max_length=50, verbose_name='Background color'),
        ),
    ]
