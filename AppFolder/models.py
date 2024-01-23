from django.db import models

# Create your models here.
class Teachers(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    online = models.BooleanField(default=False)
    def _str_(self):
        return f"{self.username}{self.email}{self.online}"
