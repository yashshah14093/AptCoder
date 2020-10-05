from django.db import models

# Create your models here.
class Teacher(models.Model):
	firstName = models.CharField(max_length = 15)
	lastName  = models.CharField(max_length = 15)
	username  = models.CharField(max_length  = 20)
	password  = models.CharField(max_length  = 20)
	email     = models.CharField(max_length=200)
	phone     = models.CharField(max_length=13)


class TeacherCourse(models.Model):
	sno = models.AutoField(primary_key = True)
	teacher = models.CharField(max_length = 20)
	course = models.CharField(max_length = 10)

	def __str__(self):
		return self.teacher + " " + self.course



class ChatBox(models.Model):
	sno = models.AutoField(primary_key = True)
	sender = models.CharField(max_length = 20)
	receiver = models.CharField(max_length = 20)
	message = models.CharField(max_length = 1500)

	def __str__(self):
		return self.sender + " " + self.receiver