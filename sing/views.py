from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req, "index.html")


def singup(req):
	return render(req, "singup.html")


def singin(req):
	return render(req, "singin.html")

def singinteacher(req):
	return render(req, "singinTeacher.html")

def singupteacher(req):
	return render(req, "singupTeacher.html")