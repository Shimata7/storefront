from django.urls import include, path
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from pprint import pprint


router = routers.DefaultRouter() #SimpleRouter()
router.register('products', views.ProductViewSet,basename='product')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
product_router.register('images', views.ProductImageViewSet, basename='product-images')
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    #path('products/', views.product_list), #path cuando se usa api view como función
    #path('products/', views.ProductList.as_view()),
    #path('products/<int:id>/', views.product_detail), #path cuando se usa api view como función
    #path('products/<int:pk>/', views.ProductDetail.as_view()),
    #path('collections/', views.CollectionList.as_view()),
    #path('collections/', views.collection_list), #path cuando se usa api view como función
    #path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
]
