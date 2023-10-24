from rest_framework.serializers import ModelSerializer
from monTiGMagasin.models import InfoProduct

class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'unit', 'availability', 'sale', 'discount', 'comments', 'owner', 'quantityInStock')


class InfoPutPriceSerializerPut(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('tig_id','discount',)
        
class InfoPutPriceSerializerRemove(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('tig_id',)
        
        
class InfoPutPriceSerializeronchange(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('tig_id',)
        
