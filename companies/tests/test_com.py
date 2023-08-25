import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture()
def force_authentication(api_client, admin):
    api_client.force_authenticate(user=admin)


def test_organizations(api_client, make_data, force_authentication):
    response = api_client.get('/organizations/1', follow=True)
    assert response.status_code == 200
    assert response.json()[0]['title'] == 'company 1'


def test_company(api_client, make_data):
    response = api_client.get('/company/2', follow=True)
    assert response.status_code == 200
    company = response.json()
    assert company['title'] == 'company 1'
    assert company['category'] == 'cat 1'
    assert len(company['districts']) == 1
    assert len(company['goods']) == 1
    assert company['company_net'] == 'net 1'


def test_creating_goods(api_client, make_data):
    response = api_client.post('/create-goods/', {
        'title': 'very goods',
        'price': 11.1,
        'company': [make_data['company'].pk]
    })
    assert response.status_code == 201
    goods = response.json()
    assert goods['title'] == 'very goods'
    assert goods['price'] == '11.10'
    assert len(goods['company']) == 1


def test_goods_detail(api_client, make_data):
    response = api_client.get('/goods/5')
    assert response.status_code == 200
    goods = response.json()
    assert goods['title'] == 'goods 1'
    assert goods['price'] == '10.40'
    assert len(goods['company']) == 1

