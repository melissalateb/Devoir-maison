from telnetlib import STATUS
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoPutPriceSerializerRemove, InfoPutPriceSerializeronchange, InfoPutPriceSerializerPut, InfoProductSerializer

# Create your views here.
class InfoProductList(APIView):
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
class InfoProductDetail(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)


class PutOnSaleView(APIView):
    def put(self, request, tig_id, newprice):
        try:
            newprice_float = float(newprice)
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.sale = True
            product.discount = newprice_float
            product.save()

            # Sérialisez l'objet InfoProduct avant de le renvoyer
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)  # Renvoie uniquement l'objet modifié
        except (InfoProduct.DoesNotExist, ValueError):
            return Response({'message': 'Product not found or invalid newprice'}, status=Http404)


class RemoveSaleView(APIView):
    def put(self, request, tig_id):
        try:
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.sale = False
            product.discount = 0
            product.save()

            # Sérialisez l'objet InfoProduct avant de le renvoyer
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)  # Renvoie uniquement l'objet modifié
        except InfoProduct.DoesNotExist:
            return Response({'message': 'Product not found'}, status=404)

class IncrementStockView(UpdateAPIView):
    queryset = InfoProduct.objects.all()
    serializer_class = InfoPutPriceSerializeronchange
    lookup_field = 'tig_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        increment_by = int(self.kwargs['number'])
        instance.quantityInStock += increment_by
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DecrementStockView(UpdateAPIView):
    queryset = InfoProduct.objects.all()
    serializer_class = InfoPutPriceSerializeronchange
    lookup_field = 'tig_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        decrement_by = int(self.kwargs['number'])
        instance.quantityInStock -= decrement_by
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)