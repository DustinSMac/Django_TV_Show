from django.db import models
import datetime

# Create your models here.
class showManager(models.Manager):
    def basic_validator(self,post_data):
        errors={}
        if len(post_data['title']) < 2:
            errors['name'] = "Title should have at least 2 characters"
        if len(post_data['network']) < 2:
            errors['network'] = "Network should have at least 2 characters"
        if post_data['description'] and len(post_data['description'])<2:
            errors['description'] = "Description should have at least 2 characters"
        return errors
class show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField(null=True, blank=True)
    create_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    objects=showManager()
    def __repr__(self):
        return f"Title: {self.title} Description: {self.description} ID: {self.id} Network: {self.network}, Release Date: {self.release_date}, Created At: {self.create_at}, Updated At: {self.updated_at}"
