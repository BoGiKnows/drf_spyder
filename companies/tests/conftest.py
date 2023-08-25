import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_spyder.settings_dev")
import django
django.setup()
import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from companies.models import District, Good, Company, CompanyNet, Category


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture()
def admin():
    user = User(
        username="admin",
        is_superuser=True,
        is_staff=True,
    )
    user.set_password("admin")
    user.save()
    return user


@pytest.fixture()
def make_data():
    district = District.objects.create(title='District 1')
    cat = Category.objects.create(title='cat 1')
    company_net = CompanyNet.objects.create(title='net 1')
    company = Company.objects.create(title='company 1', category=cat, company_net=company_net)
    company.districts.add(district)
    good = Good.objects.create(title='goods 1', price=10.40)
    good.company.add(company)

    return {
        'district': district,
        'cat': cat,
        'company_net': company_net,
        'company': company,
        'goods': good,
    }
