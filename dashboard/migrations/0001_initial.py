# Generated by Django 3.2 on 2021-04-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Towel', 'Towel'), ('Chaddar', 'Chaddar'), ('Bedsheet', 'Bedsheet'), ('Home Decor', 'Home Decor'), ('Kids', 'Kids'), ('Saree', 'Saree'), ('Dress Material', 'Dress Material'), ('Other', 'Other')], max_length=255)),
                ('main_photo', models.ImageField(blank=True, upload_to='photos/')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
