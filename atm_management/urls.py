from django.urls import path
from atm_management.views import inputdata, delete_item, update_item

urlpatterns = [
    path('', inputdata, name='inputdata'),
    path('update/<str:bid>/', update_item, name='update_item'),
    path('delete_item/<str:bid>/', delete_item, name='delete_item'),
]