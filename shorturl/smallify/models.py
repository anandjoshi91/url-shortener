from django.db import models
from django.utils.baseconv import base64


class URL(models.Model):
    original_url = models.CharField(max_length=300, unique= True)
    shortened_url = models.CharField(max_length=30, unique =  True)
    
    def shorten_url(self):
        self.shortened_url = self.__fnv_hash(self.original_url)
        
        if(len(self.shortened_url) >= len(self.original_url)):
            self.shortened_url =  self.original_url
        
        
    @staticmethod
    def __fnv_hash(key):
        h = 2166136261
        
        for k in key:
            h = (h*16777619)^ord(k)
        
        # Return 8 bit URL
        return base64.encode(h%281474976710656)
    
    def __str__(self):
        return models.Model.__str__(self)  