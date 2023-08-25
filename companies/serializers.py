from rest_framework import serializers
from companies.models import Company, Good


class CompanySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    districts = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    goods = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    company_net = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Company
        fields = ('title', 'category', 'districts', 'goods', 'company_net')


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('title',)


class CreateGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('title', 'price', 'company')


class GoodsDetailSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Good
        fields = ('title', 'price', 'company')