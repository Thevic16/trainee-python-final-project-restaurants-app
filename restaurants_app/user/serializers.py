from rest_framework import serializers

from restaurant.models import Restaurant
from user import google

from user.register import register_social_user


class GoogleSocialAuthClientSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name,
            user_role='Client', restaurant_id=None, branch_id=None)


class GoogleSocialAuthRestaurantAdministratorSerializer(
    serializers.Serializer):
    auth_token = serializers.CharField()
    restaurant_id = serializers.IntegerField(allow_null=True)

    def validate(self, attrs):

        user_data = google.Google.validate(attrs.get('auth_token'))
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id,
            email=email, name=name,
            user_role='Restaurant Administrator',
            restaurant_id=int(attrs.get('restaurant_id'), branch_id=None))


class GoogleSocialAuthEmployeeSerializer(
    serializers.Serializer):
    auth_token = serializers.CharField()
    branch_id = serializers.IntegerField(allow_null=True)

    def validate(self, attrs):

        user_data = google.Google.validate(attrs.get('auth_token'))
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id,
            email=email, name=name,
            user_role='Employee',
            restaurant_id=None, branch_id=int(attrs.get('branch_id')))


class GoogleSocialAuthBranchManagerSerializer(
    serializers.Serializer):
    auth_token = serializers.CharField()
    branch_id = serializers.IntegerField(allow_null=True)

    def validate(self, attrs):

        user_data = google.Google.validate(attrs.get('auth_token'))
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id,
            email=email, name=name,
            user_role='Branch Manager',
            restaurant_id=None, branch_id=int(attrs.get('branch_id')))