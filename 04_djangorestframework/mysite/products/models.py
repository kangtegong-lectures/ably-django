# Create your models here.
from django.db import models
from django.conf import settings


class Company(models.Model):
    com_id = models.AutoField(primary_key=True, null=False, blank=False)
    com_name = models.CharField(max_length=30)  
    com_stars = models.IntegerField(default=0)

    def __str__ (self): 
        return self.com_name

class Product(models.Model):
    SIZES = (
        ('F', 'Free'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    COLORS = (
        ('WHITE', 'White'),
        ('BLACK', 'Black'),
        ('GRAY', 'Gray'),
        ('BLUE', 'Blue'),
        ('RED', 'Red'),
        ('PINK', 'Pink'),
    ) 

    TYPES = (
        ('OUTER', 'Outer'),
        ('ONEPEICE', 'Onepeice'),
        ('PANTS', 'Pants'),
        ('SKIRT', 'Skirt'),
        ('TRAINING', 'Training'),
        ('BACKPACK', 'Backpack'),
        ('SHOES', 'Shoes'),
    ) 

    p_id = models.AutoField(primary_key=True, null=False, blank=False)
    p_type = models.TextField(max_length=10, choices=TYPES)
    p_size = models.CharField(max_length=10, choices=SIZES)
    p_color = models.CharField(max_length=10, choices=COLORS)
    p_name = models.CharField(max_length=30)
    p_price = models.IntegerField()
    p_stars = models.IntegerField(default=0)
    p_description = models.TextField()
    p_buy_count = models.IntegerField(default=0)
    p_release_date = models.DateField()
    p_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', blank=True, null=True)
    
    class Meta:
        ordering = ['p_buy_count']

    def __str__ (self): 
        return self.p_name

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image') 
    image = models.ImageField(default='media/default_image.jpeg', upload_to='product', blank=False, null=False)

class Reviews(models.Model):
    REVIEW = (
        ('5', 'Very Good'),
        ('4', 'Good'),
        ('3', 'So So'),
        ('2', 'Bad'),
        ('1', 'Very Bad'),
    )
    re_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='re_product')
    re_rate = models.CharField(max_length=10, choices=REVIEW)
    # re_user = models.ForeignKey(User, on_delete=models.CASCADE)
    re_comments = models.TextField()

class ReviewImage(models.Model):
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='img_review')
    image = models.ImageField(default='media/diary/default_image.jpeg', upload_to='reviews', blank=True, null=True)
    # image = models.ImageField(default='media/diary/default_image.jpeg', upload_to="clothes/%Y/%m/%d", blank=True, null=True)


# Detailed Info?

# User
    # userinfo
    # reviews       one to many
    # cart          one to many