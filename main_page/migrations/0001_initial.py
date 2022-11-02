# Generated by Django 4.1.2 on 2022-11-02 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user', models.CharField(max_length=110)),
                ('count', models.IntegerField()),
                ('sum', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=35)),
                ('category_added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=110)),
                ('product_price', models.FloatField()),
                ('product_des', models.TextField()),
                ('product_count', models.IntegerField()),
                ('product_date_add', models.DateTimeField(auto_now_add=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product_quantity', models.IntegerField()),
                ('cart_date_add', models.DateTimeField(auto_now_add=True)),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.product')),
            ],
        ),
    ]
