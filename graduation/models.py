from django.db import models


class Guest(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    email = models.EmailField(
        verbose_name='Email',
        unique=True,
    )

    message = models.TextField(
        verbose_name='Mensagem',
        blank=True,
        null=True,
    )

    picture = models.ImageField(
        verbose_name='Foto',
        upload_to='guests/',
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Data de confirmação',
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'
        ordering = ['-created_at']
