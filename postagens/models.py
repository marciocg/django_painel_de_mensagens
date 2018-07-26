from django.db import models

class Postagem(models.Model):
    texto = models.TextField()


    def __str__(self):
        """Representação em string do modelo."""
        return self.texto[:100]
