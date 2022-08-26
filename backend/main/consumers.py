from django.contrib.auth.models import User
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import RetrieveModelMixin, \
    UpdateModelMixin
# from djangochannelsrestframework.permissions import IsAuthenticated

from main.models import BoardData
from main.serializers import BoardDataModelSerializer


class BoardDataConsumerDetail(GenericAsyncAPIConsumer, RetrieveModelMixin,
                              UpdateModelMixin):
    """Consumer для данных доски"""
    queryset = BoardData.objects.all()
    serializer_class = BoardDataModelSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        # user = self.scope['user']
        user = User.objects.get(id=1)
        board = self.scope['url_route']['kwargs']['pk']
        return BoardData.objects.filter(board=board, board__group=user,
                                        board__is_active=True)


"""
const ws = new WebSocket("ws://localhost:8000/ws/boards/1/view/")
ws.onopen = function(){
    ws.send(JSON.stringify({
        action: "retrieve",
        request_id: new Date().getTime(), pk: 1
    }))
}
ws.onmessage = function(e){
    console.log(e.data)
}
"""
