
from typing import Tuple
from django.db import models






class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    

    class Meta:
        abstract = True

















