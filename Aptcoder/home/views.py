from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import Contact

# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')


def contact(request):
	
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		content = request.POST['content']
		
		if(len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 10):
			messages.error(request, 'Fill the form correctly')
		else:
			messages.success(request, 'Your Problem is Successfully Submitted')
			contact = Contact(name = name, email = email, phone = phone, content = content)
			contact.save()
	
	return render(request, 'home/contact.html')

