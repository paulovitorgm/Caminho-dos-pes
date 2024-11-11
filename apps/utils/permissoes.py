from rest_framework.permissions import BasePermission


class PermissaoAutenticacao(BasePermission):
    def has_permission(self, request, view):  # noqa
        permissoes = ['create', 'list', 'retrieve']

        if request.user.is_superuser:
            return view.action in permissoes + [
                'update',
                'partial_update',
                'destroy',
            ]

        elif request.user.is_staff:
            return view.action in permissoes + ['update', 'partial_update']

        elif request.user.is_anonymous:
            return view.action == 'create'

        else:
            return False
