from rest_framework import serializers

from api.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['name']

    def create(self, request):
        images_all = self.context.get('view').request.FILES
        for img in images_all.getlist('image'):
            # print(request['name'])
            Image.objects.create(name=request['name'], image=img)
        queryset = Image.objects.all()
        # print(queryset)
        return queryset


class ImageView(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['name', 'image']


