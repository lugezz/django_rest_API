from api.permissions import isStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [isStaffEditorPermission]
