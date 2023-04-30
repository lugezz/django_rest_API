from rest_framework.permissions import IsAdminUser

from api.permissions import isStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [IsAdminUser, isStaffEditorPermission]


class UserQuerysetMixin():
    user_field = 'user'
    allow_staf_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        # Allowing staff users to access to every item
        if user.is_staff and self.allow_staf_view:
            return qs
        return qs.filter(**lookup_data)
