from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField('Created at', auto_now_add=True)
    updated_date = models.DateTimeField('Last Updated at', auto_now_add=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class ContactResponse(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.email} - {self.subject}"
