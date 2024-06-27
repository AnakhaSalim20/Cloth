from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('login/', views.loginpage, name='loginpage'),
    path('adminindex',views.admin,name='admin'),
    path('logout_request/', views.logout_request, name='logout_request'),
    path('checkout',views.checkout, name='checkout'),
    path('logbook',views.log,name='log'),
    path('faq', views.faq, name='faq'),
    path('terms', views.terms, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
   # path('shop/',views.shop,name='shop'),
    #path('shop/men/', views.men, name='men'),
    #path('shop/women/', views.women, name='women'),
    path('collect/',views.collect,name='collect'),
    path('collect/bag/',views.bag,name='bag'),
    path('collect/bag/check/',views.check,name='check'),
    path('cart/',views.cart,name='cart'),
    path('ship/',views.ship,name='ship'),
    path('top',views.top,name='top'),
    path('coat',views.coat,name='coat'),
    path('tshirts',views.tshirts,name='tshirts'),
    path('skirts',views.skirt,name='skirt'),
    path('bottom',views.bottom,name='bottom'),
   # path('shops/', views.shop_list, name='shop_list'),
   # path('shops/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    #path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    ]








