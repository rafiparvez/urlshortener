from datetime import datetime
from hashlib import sha512

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Length of hash
HASH_LEN = 8

# Create your models here.

class UrlModel(models.Model):
    url = models.URLField(unique=True)
    hashed_url = models.URLField(unique=True)
    num_url_clicks = models.IntegerField(default=0)
    url_clicked_at = ArrayField(models.DateTimeField(blank=True), default=list)
    url_click_clients = ArrayField(
        models.CharField(max_length=100,blank = True), default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def get_hashed_str(self, s, str_len=8):
        """
        Get hexadecimal string with given length from a string using sha512
        """
        if not s or s=='':
            raise ValueError("string cannot be null or empty")
        if str_len > 128:
            raise ValueError("{str_len} exceeds 128".format(str_len))
        hash_object = sha512(s.encode())
        hash_hex = hash_object.hexdigest()
        return hash_hex[0:str_len]

    # override save method
    def save(self, *args, **kwargs):
        if not self.id:
            self.hashed_url = self.get_hashed_str(self.url, HASH_LEN)
        return super().save(*args, **kwargs)

    def add_url_click(self):
        self.num_url_clicks += 1
        # TODO: Implement fetching request IP
        self.url_click_clients.append("127.0.0.1")
        self.url_clicked_at.append(datetime.now())
        self.save()
