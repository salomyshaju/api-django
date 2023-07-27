# Generated by Django 4.2.2 on 2023-07-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
