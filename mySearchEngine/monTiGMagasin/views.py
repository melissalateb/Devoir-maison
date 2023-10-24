from telnetlib import STATUS
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoProductSerializer

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


# class put_on_sale(APIView):
#     def put(self, request, tig_id, newprice, format=None):
#         try:
#             product = InfoProduct.objects.get(tig_id=tig_id)
#         except InfoProduct.DoesNotExist:
#             raise Http404
#         product.sale = True
#         product.discount = newprice
#         product.save()
        
#         serialize = InfoProductSerializer(product)
#         return Response(serialize.data)

# class remove_sale(APIView):
#     def put(self, request, tig_id, newprice, format=None):
#         try:
#             product = InfoProduct.objects.get(tig_id=tig_id)
#         except InfoProduct.DoesNotExist:
#             raise Http404

#         product.sale = False
#         product.discount = 0.0
#         product.save()

#         serializer = InfoProductSerializer(product)
#         return Response(serializer.data)



class PutOnSaleView(UpdateAPIView):
    queryset = InfoProduct.objects.all()
    serializer_class = InfoProductSerializer
    lookup_field = 'tig_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.sale = True
        instance.discount = float(self.kwargs['newprice'])
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RemoveSaleView(UpdateAPIView):
    queryset = InfoProduct.objects.all()
    serializer_class = InfoProductSerializer
    lookup_field = 'tig_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.sale = False
        instance.discount = 0
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)