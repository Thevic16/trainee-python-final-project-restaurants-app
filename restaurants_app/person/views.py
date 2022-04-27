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
        An endpoint that allows authenticating a person with the HTTP method
         post, based on a google token. Everybody has permission to access
          this resource.
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class SocialAuthClientView(GenericAPIView):
    permission_classes = []
    serializer_class = SocialAuthClientSerializer
    """
    An endpoint that allows using of the HTTP method post to create with
     the person with the client role. Everybody has permission to access
      this resource.
    """

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class SocialAuthRestaurantAdministratorView(GenericAPIView):
    permission_classes = [IsPortalManager]
    serializer_class = SocialAuthRestaurantAdministratorSerializer
    """
    An endpoint that allows using of the HTTP method post to create with
     the person with the restaurant role. Only the portal manager role
      has permission to access this resource.
    """

    def post(self, request):
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
    """
    An endpoint that allows using of the HTTP method post to create with
     the person with the employees role. Only the restaurant-administrators
      role has permission to access this resource.
    """

    def post(self, request):
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
    """
    An endpoint that allows using of the HTTP method post to retrieve the token
     of the portal manager user (remember first run the command to generate the
      portal manager user). Everybody has permission to access this resource,
       however you have to know the credentials to access it.
    """
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = SocialAuthBranchManagerSerializer

    def post(self, request):
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
    """
    An endpoint that allows using of the HTTP method post to retrieve the
    token of the portal manager user (remember first run the command to
    generate the portal manager user). Everybody has permission to access
    this resource, however you have to know the credentials to access it.
    """

    def post(self, request):
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
