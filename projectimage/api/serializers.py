from rest_framework import serializers

from api.models import Image, Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='image_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['p_id', 'name', 'images']

    def create(self, request):
        images_all = self.context.get('view').request.FILES
        print(request)
        product = Product.objects.create(p_id=request['p_id'], name=request['name'])
        for image in images_all.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product
