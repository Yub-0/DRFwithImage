from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Image
from api.serializers import ImageSerializer, ImageView


class ViewImage(generics.GenericAPIView):

    queryset = Image.objects.all()

    def get(self, request):
        product = self.get_queryset()
        serializer = ImageView(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadImage(generics.GenericAPIView):
    serializer_class = ImageSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error)
