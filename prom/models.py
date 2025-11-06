from django.db import models


class PromGuest(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Sobrenome'
    )
    confirmed_presence = models.BooleanField(default=False, verbose_name='Presença')
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()

    def __str__(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()
