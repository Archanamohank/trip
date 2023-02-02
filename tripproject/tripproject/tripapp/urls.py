from.import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('',views.test,name='test')
     # path('add/',views.addition,name='addition')
]