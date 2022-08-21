from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Board, BoardData
from main.permissions import BoardDataListOnly
from main.serializers import BoardModelSerializer, BoardDataModelSerializer


class BoardListApiView(generics.ListAPIView, generics.CreateAPIView):
    """ApiView для досок"""
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer

    def perform_create(self, serializer):
        group = serializer.validated_data['group']
        author = self.request.user
        if author.pk not in group:
            group.append(author.pk)
        serializer.save(author=author, group=group)

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(is_active=True, group=user)


class BoardDetailApiView(generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.DestroyAPIView):
    """ApiView для доски"""
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer

    def get_queryset(self):
        user = self.request.user
        board = self.kwargs['pk']
        return Board.objects.filter(id=board, group=user, is_active=True)

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs['pk']
        board = Board.objects.filter(id=pk, author=user)
        if board:
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data={"detail": "У вас недостаточно прав "
                            "для выполнения данного действия."})
    
    def update(self, request, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs['pk']
        board = Board.objects.filter(id=pk, author=user)
        if board:
            return super().update(request, *args, **kwargs)
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data={"detail": "У вас недостаточно прав "
                            "для выполнения данного действия."})


class BoardDataListApiView(generics.RetrieveAPIView, generics.UpdateAPIView):
    """ApiView для списка данных доски"""
    queryset = BoardData.objects.all()
    serializer_class = BoardDataModelSerializer
    permission_classes = [IsAuthenticated, BoardDataListOnly]

    def get_queryset(self):
        user = self.request.user
        board = self.kwargs['pk']
        return BoardData.objects.filter(board=board, board__group=user,
                                        board__is_active=True)

    # def perform_create(self, serializer):
    #     board = Board.objects.get(id=self.kwargs['pk'])
    #     serializer.save(board=board)


# class BoardDataDetailApiView(generics.RetrieveAPIView, generics.UpdateAPIView):
#     """ApiView для данных доски"""
#     queryset = BoardData.objects.all()
#     serializer_class = BoardDataModelSerializer
#
#     def get_object(self):
#         user = self.request.user
#         board = self.kwargs['pk']
#         board_data = {self.lookup_field: self.kwargs['pk_id']}
#         obj = get_object_or_404(self.queryset.filter(
#             id=board_data['pk'], board=board, board__group=user,
#             board__is_active=True), **board_data)
#         self.check_object_permissions(self.request, obj)
#         return obj
