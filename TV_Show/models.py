from django.db import models

# Create your models here.
class show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField(null=True, blank=True)
    create_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __repr__(self):
        return f"Title: {self.title} Description: {self.description} ID: {self.id} Network: {self.network}, Release Date: {self.release_date}"