from django.urls import path, register_converter
from monTiGMagasin import views
from .converters import FloatConverter
from .views import PutOnSaleView, RemoveSaleView, DecrementStockView, IncrementStockView

register_converter(FloatConverter, 'float')

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    # Exercice2:
    #dans les champs d’information correspondant au
    #produit id, affecter le champs sale à TRUE, en même temps, affecter le champs discount avec la valeur
    #newprice, puis, retourner les informations de ce produit après la mise à jour.
    # path('putonsale/<int:tig_id>/<float:newprice>/', views.put_on_sale.as_view()),
    # dans les champs d’information correspondant au produit id, affecter le
    # champs sale à FALSE, puis, retourner les informations de ce produit après la mise à jou
    # path('removesale/<int:tig_id>/', views.remove_sale.as_view()),
    
    
    path('putonsale/<int:tig_id>/<str:newprice>/', PutOnSaleView.as_view(), name='putonsale'),
    # path('putonsale/', PutOnSaleView.as_view()),
    path('removesale/<int:tig_id>/', RemoveSaleView.as_view(), name='removesale'),
    
    #Exercice 3 : increment and decrement the stock
    path('incrementStock/<int:tig_id>/<int:number>/', IncrementStockView.as_view(), name='increment_stock'),
    path('decrementStock/<int:tig_id>/<int:number>/', DecrementStockView.as_view(), name='decrement_stock'),
]