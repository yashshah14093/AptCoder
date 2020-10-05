from django.db import models

# Create your models here.
class Student(models.Model):
	firstName = models.CharField(max_length = 15)
	lastName  = models.CharField(max_length = 15)
	username  = models.CharField(max_length  = 20)
	password  = models.CharField(max_length  = 20)
	email     = models.CharField(max_length=200)
	phone     = models.CharField(max_length=13)



class StudentCourse(models.Model):
	sno = models.AutoField(primary_key = True)
	student = models.CharField(max_length = 20)
	course = models.CharField(max_length = 10)

	def __str__(self):
		return self.student + " " + self.course