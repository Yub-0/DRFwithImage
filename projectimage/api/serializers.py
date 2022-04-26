from rest_framework import serializers

from api.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['name']

    def create(self, validated_data):
        images_all = self.context.get('view').request.FILES
        for img in images_all.getlist('image'):
            queryset = Image.objects.create(name=validated_data.get('name'), image=img)
        return queryset


class ImageView(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['name', 'image']


