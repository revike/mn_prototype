from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Board(models.Model):
    """Модель доски"""

    objects = None

    class Meta:
        verbose_name_plural = 'доски'
        verbose_name = 'доски'

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name='автор')
    group = models.ManyToManyField(User, blank=True, related_name='group',
                                   verbose_name='группа')
    name = models.CharField(max_length=120, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    created = models.DateTimeField(auto_now_add=True, verbose_name='создание')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновление')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='активна')

    def __str__(self):
        return f'{self.name}'


class BoardData(models.Model):
    """Модель данных на доске"""
    objects = None

    class Meta:
        verbose_name_plural = 'данные доски'
        verbose_name = 'данные доски'

    board = models.OneToOneField(Board, on_delete=models.CASCADE,
                                 verbose_name='доска')
    data = models.JSONField(verbose_name='данные')
    user_update = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='обновление')

    @receiver(post_save, sender=Board)
    def create_board_data(sender, instance, created, **kwargs):
        data = {
            'x': {
                'black': [],
                'red': [],
                'green': [],
                'blue': [],
                'yellow': [],
                'orange': [],
                'purple': []
            },
            'y': {
                'black': [],
                'red': [],
                'green': [],
                'blue': [],
                'yellow': [],
                'orange': [],
                'purple': []
            }
        }
        if created:
            BoardData.objects.create(board=instance, data=data)

    def __str__(self):
        return f'{self.board.name}'
