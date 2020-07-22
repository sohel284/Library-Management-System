from django.db import models

from core.models import BaseModel
from book.models import CopyOfBook
from user.models import User


class Borrow(BaseModel):
    borrow_book = models.ForeignKey(CopyOfBook, on_delete=models.PROTECT, related_name='borrow', )
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='borrow', )
    issue_date = models.DateField(auto_now_add=True, verbose_name='Date Of Issue', )
    return_date = models.DateField(null=True, blank=True, verbose_name='Date Of Return', )
    
    class Meta:
        db_table = 'borrows'
        verbose_name = 'Borrow'
        verbose_name_plural = 'Borrows'
        
    def user_name(self):
        return self.user.get_full_name()

    
