from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    """Админ или только для просмотра товара"""

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class IsReviewAuthorOrAdmin(BasePermission):
    """Автор отзыва на товар или админ"""
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated or
            request.user and request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            obj.author == request.user or
            request.user and request.user.is_staff
        )
