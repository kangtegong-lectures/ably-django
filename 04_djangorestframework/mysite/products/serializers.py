from .models import Product, Company, ProductImage
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class CompanySerializer(serializers.ModelSerializer):
    
    com_stars = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']

class ProductSerializer(serializers.ModelSerializer):

    image = ProductImageSerializer(many=True)
    p_stars = serializers.IntegerField(read_only=True)
    p_buy_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ['p_id', 'p_type', 'p_size', 'p_color', 'p_name', 'p_price', 'p_stars', 'p_description', 'p_buy_count', 'p_release_date', 'p_company', 'image']

    # create와 
    # def create(self, validated_data): 
    #     image_data = validated_data.pop('image')
    #     product = Product.objects.create(**validated_data)
    #     ProductImage.objects.create(product=product, **image_data)
    #     return product
    
    ## def update

