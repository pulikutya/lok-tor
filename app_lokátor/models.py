from django.db import models

# Create your models here.

class hely(models.Model):
    
    

    class Meta:
        verbose_name="hely"
        verbose_name_plural="helyek"
    def __str__(self):
        return self.name
    #def get_absolute_url(self):
    #    return reverse("hely_detail", kwargs={"pk": self.pk})
