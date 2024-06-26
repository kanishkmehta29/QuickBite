from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index , name = 'index') , 
    path('foodplace/<str:pk>',views.foodplace ,name = 'foodplace'),
    path('signup',views.signup,name = 'signup'),
    path('signup1',views.signup1,name = 'signup1'),
    path('login',views.login,name = 'login') , 
    path('logout' , views.logout , name = 'logout'),
    path('addsection/<str:pk>' , views.addsection , name = 'addsection'),
    path('subsection/<str:pk1>/<str:pk2>' , views.subsection , name = 'subsection'),
    path('addsubsection/<str:pk1>/<str:pk2>' , views.addsubsection , name = 'addsubsection') , 
    path('order/<str:pk>' , views.order , name = 'order') , 
    path('addfoodsection' , views.addfoodsection , name = 'addfoodsection') , 
    path('confirmorder/<str:pk>' , views.confirmorder , name = 'confirmorder') , 
    path('orderlog/<str:pk>' , views.orderlog , name = 'orderlog' ) , 
    path('ordersreceived/<str:pk>' , views.ordersreceived , name = 'ordersreceived' ) , 
    path('activate/<uidb64>/<token>/', views.activate, name='activate')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)