from django.contrib import admin

from main.models import Board, BoardData


class InlineBoardData(admin.StackedInline):
    model = BoardData
    extra = 0

    def has_add_permission(self, request, obj):
        pass


class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineBoardData]


admin.site.register(Board, BoardAdmin)
admin.site.register(BoardData)
