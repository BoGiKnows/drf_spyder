from django.urls import path
from companies.views import GetCompaniesByDistrict, GetCompany, CreateGoods, GoodsDetail

urlpatterns = [
    path('organizations/<int:pk>/', GetCompaniesByDistrict.as_view()),
    path('company/<int:pk>/', GetCompany.as_view()),
    path('create-goods/', CreateGoods.as_view()),
    path('goods/<int:pk>', GoodsDetail.as_view())
]
