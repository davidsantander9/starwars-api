# Generated by Django 3.0.8 on 2022-05-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starships', '0003_auto_20220508_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='cargo_capacity',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='cost_in_credits',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='created',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='edited',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='length',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='max_atmosphering_speed',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='starship',
            name='url',
            field=models.CharField(default='', max_length=120),
        ),
    ]
