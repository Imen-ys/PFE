from django.db import models

class Message(models.Model):
    user_name = models.CharField(max_length=100)
    domain_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user_name}  {self.domain_name}  {self.description}"
