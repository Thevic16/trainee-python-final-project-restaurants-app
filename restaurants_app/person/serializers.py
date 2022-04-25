from rest_framework import serializers
from person import google
from person.register import register_social_user, authenticate_portal_manager


class GoogleSocialAuthSerializer(serializers.Serializer):
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
            user_role=None, restaurant_id=None, branch_id=None)


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
            restaurant_id=attrs.get('restaurant_id'), branch_id=None)


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
            restaurant_id=None, branch_id=attrs.get('branch_id'))


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
            restaurant_id=None, branch_id=attrs.get('branch_id'))


class GoogleSocialAuthPortalManagerSerializer(
    serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password',
                                            'placeholder': 'Password'})

    def validate(self, attrs):
        return authenticate_portal_manager(
            email=attrs.get('email'), password=attrs.get('password'))
