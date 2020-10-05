from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=13)
	content = models.TextField()
	dateTime = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name + " " + self.email