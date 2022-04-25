from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
from person.permissions import IsRestaurantAdministrator, IsPortalManager
from person.serializers import \
    (GoogleSocialAuthClientSerializer,
     GoogleSocialAuthRestaurantAdministratorSerializer,
     GoogleSocialAuthEmployeeSerializer,
     GoogleSocialAuthBranchManagerSerializer,
     GoogleSocialAuthPortalManagerSerializer, GoogleSocialAuthSerializer
     )

from utilities.logger import Logger


class GoogleSocialAuthView(GenericAPIView):
    permission_classes = []
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class GoogleSocialAuthClientView(GenericAPIView):
    permission_classes = []
    serializer_class = GoogleSocialAuthClientSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class GoogleSocialAuthRestaurantAdministratorView(GenericAPIView):
    permission_classes = [IsPortalManager]
    serializer_class = GoogleSocialAuthRestaurantAdministratorSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        try:
            serializer = self.serializer_class(data=request.data)
            Logger.debug(f'serializer: {serializer}')
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        return Response(data, status=status.HTTP_200_OK)


class GoogleSocialAuthEmployeeView(GenericAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = GoogleSocialAuthEmployeeSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        try:
            serializer = self.serializer_class(data=request.data)
            Logger.debug(f'serializer: {serializer}')
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        return Response(data, status=status.HTTP_200_OK)


class GoogleSocialAuthBranchManagerView(GenericAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = GoogleSocialAuthBranchManagerSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        try:
            serializer = self.serializer_class(data=request.data)
            Logger.debug(f'serializer: {serializer}')
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        return Response(data, status=status.HTTP_200_OK)


class GoogleSocialAuthPortalManagerView(GenericAPIView):
    serializer_class = GoogleSocialAuthPortalManagerSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        try:
            serializer = self.serializer_class(data=request.data)
            Logger.debug(f'serializer: {serializer}')
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data

        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)
        except AuthenticationFailed:
            return Response('Authentication Failed')

        return Response(data, status=status.HTTP_200_OK)
