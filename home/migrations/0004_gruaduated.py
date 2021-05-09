# Generated by Django 3.2 on 2021-04-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_instructor_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gruaduated',
            fields=[
                ('id_graduated', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('document_type', models.CharField(max_length=5)),
                ('number_document', models.IntegerField(verbose_name=12)),
                ('email_adrres', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('addres', models.CharField(max_length=30)),
                ('addres_enterprise', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=4)),
                ('experencie', models.CharField(max_length=4)),
                ('available', models.CharField(max_length=4)),
                ('user_graduated', models.CharField(max_length=20)),
                ('password_graduated', models.CharField(max_length=20)),
            ],
        ),
    ]
