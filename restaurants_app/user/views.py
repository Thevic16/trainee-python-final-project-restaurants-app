from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Create your views here.
from user.serializers import GoogleSocialAuthClientSerializer


class GoogleSocialAuthClientView(GenericAPIView):
    serializer_class = GoogleSocialAuthClientSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
