from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
from person.permissions import IsRestaurantAdministrator, IsPortalManager
from person.serializers import (SocialAuthClientSerializer,
                                SocialAuthRestaurantAdministratorSerializer,
                                SocialAuthEmployeeSerializer,
                                SocialAuthBranchManagerSerializer,
                                SocialAuthPortalManagerSerializer,
                                SocialAuthSerializer
                                )

from utilities.logger import Logger


class SocialAuthView(GenericAPIView):
    permission_classes = []
    serializer_class = SocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class SocialAuthClientView(GenericAPIView):
    permission_classes = []
    serializer_class = SocialAuthClientSerializer

    def post(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from google to get person information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class SocialAuthRestaurantAdministratorView(GenericAPIView):
    permission_classes = [IsPortalManager]
    serializer_class = SocialAuthRestaurantAdministratorSerializer

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


class SocialAuthEmployeeView(GenericAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = SocialAuthEmployeeSerializer

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


class SocialAuthBranchManagerView(GenericAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = SocialAuthBranchManagerSerializer

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


class SocialAuthPortalManagerView(GenericAPIView):
    serializer_class = SocialAuthPortalManagerSerializer

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
