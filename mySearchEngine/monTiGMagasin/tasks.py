# from background_task import background
# from .models import InfoProduct


# @background(schedule=60)  # Planifiez la tâche pour s'exécuter toutes les 60 secondes (ou ajustez selon vos besoins)
# def update_promotions():
#     # Obtenez tous les produits
#     products = InfoProduct.objects.all()

#     for product in products:
#         if product.quantityInStock > 16:
#             if 16 <= product.quantityInStock <= 64:
#                 product.sale = True
#                 product.discount = 0.8 * product.price
#             else:
#                 product.sale = True
#                 product.discount = 0.5 * product.price
#         else:
#             product.sale = False
#             product.discount = 0
#         product.save()
