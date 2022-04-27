from rest_framework import permissions
from utilities.logger import Logger
from rest_framework.permissions import SAFE_METHODS


class IsPortalManager(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.role.name == 'Portal Manager':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.role.name == 'Portal Manager':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.role.name == 'Client':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.role.name == 'Client':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.role.name == 'Employee':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.role.name == 'Employee':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class IsRestaurantAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        Logger.debug(f'user:{request.user}')
        try:
            if request.user.role.name == 'Restaurant Administrator':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        Logger.debug(f'user:{request.user}')
        try:
            if request.user.role.name == 'Restaurant Administrator':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class IsBranchManager(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.role.name == 'Branch Manager':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.role.name == 'Branch Manager':
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
