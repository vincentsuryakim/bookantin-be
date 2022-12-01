from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.user_extension.type == "SELLER"
        return False

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.user_extension.type == "CUSTOMER"
        return False

class IsSellerVerified(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.user_extension.type == "SELLER" and request.user.seller.verified
        return False

class IsSellerNotVerified(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.user_extension.type == "SELLER" and not request.user.seller.verified
        return False

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.user_extension.type == "ADMIN"
        return False