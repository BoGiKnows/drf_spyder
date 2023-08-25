from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from companies.models import Company, Good
from companies.serializers import CompanySerializer, \
                                  CompanyListSerializer, \
                                  CreateGoodsSerializer, \
                                  GoodsDetailSerializer


class GetCompaniesByDistrict(generics.ListAPIView):
    serializer_class = CompanyListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['goods__title']
    filterset_fields = ['category']

    def get_queryset(self):
        return Company.objects.filter(districts=self.kwargs['pk'])


class GetCompany(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CreateGoods(generics.CreateAPIView):
    serializer_class = CreateGoodsSerializer


class GoodsDetail(generics.RetrieveAPIView):
    serializer_class = GoodsDetailSerializer
    queryset = Good.objects.all()



