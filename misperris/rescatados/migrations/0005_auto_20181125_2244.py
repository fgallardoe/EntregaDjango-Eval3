# Generated by Django 2.1.3 on 2018-11-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescatados', '0004_auto_20181125_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptantes',
            name='fono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='id_comuna',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id_region',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
