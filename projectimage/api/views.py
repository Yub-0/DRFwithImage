from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Product
from api.serializers import ProductSerializer


class ViewProducts(generics.GenericAPIView):

    queryset = Product.objects.all()

    def get(self, request):
        product = self.get_queryset()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadProduct(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error)
