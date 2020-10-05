from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from Student.models import StudentCourse
from Teacher.models import TeacherCourse,ChatBox

# Create your views here.
def studyHome(request):
	return render(request, 'Student/studyHome.html')


def handleSignUp(request):
	if(request.method == 'POST'):

		firstname = request.POST['firstname']
		lastname  = request.POST['lastname']
		username  = request.POST['username']
		Password  = request.POST['Password']
		email     = request.POST['email']
		phone     = request.POST['phone']

		user = User.objects.create_user(username, email, Password)
		user.first_name = firstname
		user.last_name  = lastname
		user.save()
		messages.success(request, "Your account is successfully created")
		return redirect('/study')

	else:
		return HttpResponse('404 - NOT FOUND')




def loginUser(request):

	if(request.method == 'POST'):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username = username, password = password)

		if(user is not None):
			login(request, user)
			messages.success(request, "Successfully, Logged in")
		else:
			messages.error(request, "Invalid Credentials")

	return redirect('/study/dashboard')




def logoutUser(request):
	logout(request)
	messages.success(request, "Successfully Logged Out")
	return redirect('/study')



def dashboard(request):
	obj = StudentCourse.objects.all()
	return render(request, 'Student/dashboard.html', {'obj':obj})



def profile(request):
	return render(request, 'Student/profile.html')


def course(request):
	obj = TeacherCourse.objects.all()
	return render(request, 'Student/course.html', {'obj':obj})


def enroll(request):
	if(request.method == 'POST'):
		username = request.POST['username']
		course = request.POST['courseCode']

		messages.success(request, 'Successfully Enrolled')
		entry = StudentCourse(student = username, course = course)
		entry.save()

	return redirect('/study/dashboard')


def chat(request):
	obj = ChatBox.objects.all()
	return render(request, 'Student/chat.html', {'obj':obj})


def send(request):
	if(request.method == 'POST'):
		receiver = request.POST['receiver']
		sender = request.POST['sender']
		message = request.POST['message']

		chatbox = ChatBox(receiver = receiver, sender = sender, message = message)
		chatbox.save()
		messages.success(request, "Message Successfully, Sent")

	return redirect('/study/chat')