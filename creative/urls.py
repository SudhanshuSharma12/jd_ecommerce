from django.urls import path
from .views import (HomeView,produ,ItemAddView,CheckoutView,PaymentView,add_to_cart,remove_from_cart,OrderSummaryView,remove_single_item_from_cart,review)

app_name = 'creative'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', produ, name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('itemadd/',ItemAddView.as_view(), name='item-add'),
    path('review/<int:id>',review, name='review'),
] 

