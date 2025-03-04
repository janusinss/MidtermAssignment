from django.shortcuts import render, redirect
from .models import Students
# Create your views here.

def index(request):
    Student = Students.objects.all()
    context = {'Student': Student}
    return render(request, 'temp/index.html', context)

def editPage(request):
    return render(request, 'temp/editPage.html')

def addStudent(request):
    FirstName = request.POST['FirstName']
    LastName = request.POST['LastName']
    Email = request.POST['Email']
    DateOfBirth = request.POST['DateOfBirth']
    Course = request.POST['Course']
    EnrollmentDate = request.POST['EnrollmentDate']

    newStudents = Students(
        FirstName = FirstName,
        LastName = LastName,
        Email = Email,
        DateOfBirth = DateOfBirth,
        Course = Course,
        EnrollmentDate = EnrollmentDate
    )
    newStudents.save()

    return redirect('/SMSApp/')

def editStudent(request, id):
    Student = Students.objects.get(id=id)
    context = {'Student':Student}

    return render(request, 'temp/editPage.html', context)

def updateStudent(request, id):
    Student = Students.objects.get(id=id)

    Student.FirstName = request.POST['FirstName']
    Student.LastName = request.POST['LastName']
    Student.Email = request.POST['Email']
    Student.DateOfBirth = request.POST['DateOfBirth']
    Student.Course = request.POST['Course']
    Student.EnrollmentDate = request.POST['EnrollmentDate']
    Student.save()

    return redirect('/SMSApp/')

def deleteStudent(request, id):
    Student = Students.objects.get(id=id)
    Student.delete()
    return redirect('/SMSApp/')