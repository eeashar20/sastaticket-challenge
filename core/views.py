from djoser.views import UserViewSet as BaseUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.models import User


# Create your views here.

class UserViewSet(BaseUserViewSet):
    @action(detail=False, permission_classes=[IsAdminUser], url_name='get_all_user_emails',
            url_path='emails')
    def get_orders_by_customer_email(self, request):
        users = User.objects.all().values_list('email', flat=True)

        if users:
            return Response(users, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)
