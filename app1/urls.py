from django.urls import path
from . import views


urlpatterns=[
    path('',views.premiumfn,name='premiumfn'),
    path('premm',views.premm,name='premm'),
    path('pair',views.pairr,name='pair'),
    path('pro',views.pro,name='pro'),
    
]