from rest_framework.permissions import BasePermission


class IsOrderOwner(BasePermission):
    """Владелец заказа или админ"""

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated or
            request.user and request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            obj.owner == request.user or
            request.user and request.user.is_staff
        )


class OrderStatusChange(BasePermission):
    """Проверка на админа"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
