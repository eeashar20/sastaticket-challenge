from rest_framework import status
import pytest
from store.models import Product

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_product_exists_returns_200(self, api_client, authenticate):
        authenticate()

        product = Product.objects.create(name="Ship", unit_price=24.52)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': product.id,
            'name': product.name,
            'unit_price': product.unit_price
        }
