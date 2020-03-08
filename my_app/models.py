from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):                          # Search object and after blah blah in admin panel
        return '{}'.format(self.search)

    class Meta:                                 # written search and after searches in admin panel
        verbose_name_plural = 'Searches'