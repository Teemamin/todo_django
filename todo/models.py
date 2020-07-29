from django.db import models


# Create your models here.
class item(models.Model):
    # inherits all the base functionality from the built-in Django model class
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        # this is to overwrite the inherited name behaviour frm django
        #  by redifining it here in our own class
        return self.name
    # this is going to return the item class's name attribute
