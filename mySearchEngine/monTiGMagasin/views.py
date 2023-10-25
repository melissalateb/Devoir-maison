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


class IncrementStockView(APIView):
    def put(self, request, tig_id, number):
        try:
            increment_by = int(number)
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.quantityInStock += increment_by
            product.save()

            # Sérialisez l'objet InfoProduct avant de le renvoyer
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)  # Renvoie uniquement l'objet modifié
        except (InfoProduct.DoesNotExist, ValueError):
            return Response({'message': 'Product not found or invalid increment'}, status=404)


class DecrementStockView(APIView):
    def put(self, request, tig_id, number):
        try:
            decrement_by = int(number)
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.quantityInStock -= decrement_by
            product.save()

            # Sérialisez l'objet InfoProduct avant de le renvoyer
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)  # Renvoie uniquement l'objet modifié
        except (InfoProduct.DoesNotExist, ValueError):
            return Response({'message': 'Product not found or invalid decrement'}, status=404)

