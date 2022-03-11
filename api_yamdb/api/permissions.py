from rest_framework import permissions


class IsRoleAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (user.is_authenticated and user.is_admin
                or user.is_superuser)

    def has_object_permission(self, request, view, obj):
        # после удаления данного пермишена падают тесты:
        # tests/test_05_review.py::Test05ReviewAPI::test_03_review_detail
        # tests/test_05_review.py::Test05ReviewAPI::test_04_reviews_check_permission
        # tests/test_06_comment.py::Test06CommentAPI::test_03_review_detail
        # tests/test_06_comment.py::Test06CommentAPI::test_04_comment_check_permission
        user = request.user
        return (user.is_authenticated and user.is_admin
                or user.is_superuser)


class IsRoleModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (user.is_authenticated and user.is_moderator
                or user.is_superuser)

    def has_object_permission(self, request, view, obj):
        # после удаления данного пермишена падают тесты:
        # tests/test_05_review.py::Test05ReviewAPI::test_03_review_detail
        # tests/test_05_review.py::Test05ReviewAPI::test_04_reviews_check_permission
        # tests/test_06_comment.py::Test06CommentAPI::test_03_review_detail
        # tests/test_06_comment.py::Test06CommentAPI::test_04_comment_check_permission
        user = request.user
        return (user.is_authenticated and user.is_moderator
                or user.is_staff)


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (user.is_authenticated and user.is_user
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
