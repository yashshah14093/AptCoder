from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from Teacher.models import TeacherCourse,ChatBox

# Create your views here.
def teachHome(request):
	return render(request, 'Teacher/teachHome.html')


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
		return redirect('/teach')

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

	return redirect('/teach/dashboard')




def logoutUser(request):
	logout(request)
	messages.success(request, "Successfully Logged Out")
	return redirect('/teach')



def dashboard(request):

	obj = TeacherCourse.objects.all()
	return render(request, 'Teacher/dashboard.html', {'obj':obj})



def profile(request):
	return render(request, 'Teacher/profile.html')


def chat(request):
	obj = ChatBox.objects.all()
	return render(request, 'Teacher/chat.html', {'obj':obj})



def send(request):
	if(request.method == 'POST'):
		receiver = request.POST['receiver']
		sender = request.POST['sender']
		message = request.POST['message']

		chatbox = ChatBox(receiver = receiver, sender = sender, message = message)
		chatbox.save()
		messages.success(request, "Message Successfully, Sent")

	return redirect('/study/chat')
