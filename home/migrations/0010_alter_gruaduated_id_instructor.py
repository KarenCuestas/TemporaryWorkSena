# Generated by Django 3.2 on 2021-04-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_gruaduated_id_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruaduated',
            name='id_instructor',
            field=models.IntegerField(default=0),
        ),
    ]