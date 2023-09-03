from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wallet
from .serializers import WalletSerializer


class WalletView(APIView):
    serializer_class = WalletSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieves the wallet object for the authenticated user and serializes it.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: The serialized wallet balance in the HTTP response with a status code of 200 (OK).
        """
        wallet = Wallet.objects.get(user=request.user)
        serializer = WalletSerializer(wallet)

        return Response(serializer.data, status=status.HTTP_200_OK)
