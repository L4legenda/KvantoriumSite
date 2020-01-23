from django.shortcuts import render

# Create your views here.
def account(req):
	return render(req, "teacher/account.html")

def groups(req):
	return render(req, "teacher/groups.html")

def students(req):
	return render(req, "teacher/students.html")

def timetable(req):
	return render(req, "teacher/timetable.html")