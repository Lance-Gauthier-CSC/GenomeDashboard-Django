from django.db import models

# Create your models here.
class Session(models.Model):
    session_id = models.CharField(primary_key=True, max_length=200, editable=False)
    file = models.FileField()
    
    def __str__(self):
        return self.session_id