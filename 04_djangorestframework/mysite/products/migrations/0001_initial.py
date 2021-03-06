# Generated by Django 3.2.9 on 2021-12-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_name', models.CharField(max_length=30)),
                ('com_stars', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_type', models.TextField(choices=[('OUTER', 'Outer'), ('ONEPEICE', 'Onepeice'), ('PANTS', 'Pants'), ('SKIRT', 'Skirt'), ('TRAINING', 'Training'), ('BACKPACK', 'Backpack'), ('SHOES', 'Shoes')], max_length=10)),
                ('p_size', models.CharField(choices=[('F', 'Free'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=10)),
                ('p_color', models.CharField(choices=[('WHITE', 'White'), ('BLACK', 'Black'), ('GRAY', 'Gray'), ('BLUE', 'Blue'), ('RED', 'Red'), ('PINK', 'Pink')], max_length=10)),
                ('p_name', models.CharField(max_length=30)),
                ('p_price', models.IntegerField()),
                ('p_stars', models.IntegerField(default=0)),
                ('p_description', models.TextField()),
                ('p_buy_count', models.IntegerField(default=0)),
                ('p_release_date', models.DateField()),
                ('p_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='products.company')),
            ],
            options={
                'ordering': ['p_buy_count'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_rate', models.CharField(choices=[('5', 'Very Good'), ('4', 'Good'), ('3', 'So So'), ('2', 'Bad'), ('1', 'Very Bad')], max_length=10)),
                ('re_comments', models.TextField()),
                ('re_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='re_product', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='media/diary/default_image.jpeg', null=True, upload_to='reviews')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img_review', to='products.reviews')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='media/default_image.jpeg', upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodcut', to='products.product')),
            ],
        ),
    ]
