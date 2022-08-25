from rest_framework.permissions import BasePermission

from main.models import BoardData, Board


class BoardDataListOnly(BasePermission):
    """Доступ для владельца доски и участника группы"""

    def has_permission(self, request, view):
        board_pk = view.kwargs['pk']
        user_pk = request.user.pk
        board_data = BoardData.objects.filter(board__is_active=True,
                                              board=board_pk,
                                              board__group=user_pk)
        board = Board.objects.filter(id=board_pk, is_active=True,
                                     group=user_pk)

        if board_data.count() or board.count():
            return True
