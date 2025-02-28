
from django.contrib import admin
from django.urls import path, include



from .api_views import *

# Ici nous créons notre routeur
# router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘product’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/product/’
# router.register('product_search', ProductSearchView, basename='api_product_search')

urlpatterns = [
    path('callback/<int:souscrip_id>/', CallbackAPIView.as_view(), name='payment_callback'),
  
    
    
]
