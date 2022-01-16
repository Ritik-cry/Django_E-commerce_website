# Generated by Django 3.2.9 on 2022-01-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=300)),
                ('phone', models.IntegerField(default='', max_length=10)),
                ('city', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
    ]
