# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from result.models import *
#from result2.models import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

def home(request):
    return direct_to_template(request,'home.html',)
def first(request):
    
    return direct_to_template(request,'search_form.html',)
def second(request):
    return direct_to_template(request,'search_form2.html',)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        stud = Student.objects.filter(student_id=q)

        var = 0
        gtot = 0
        exams = Exam.objects.filter(student_id=q)
        for itr in exams:
          gtot = gtot+itr.maximum_marks
        for tot in exams:
          var = var+tot.marks_obtained
          
        
        return direct_to_template(request,'search_results.html',{'exams':exams,'stud':stud,'total':var,'gtot':gtot,'query' : q})
        
    else: 
      
        return HttpResponse('Please Enter a Valid number')


def search2(request):
    from result2.models import *

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        stud = Student.objects.filter(student_id=q)

        var = 0
        gtot = 0
        exams = Exam.objects.filter(student_id=q)
        for itr in exams:
          gtot = gtot+itr.maximum_marks
        for tot in exams:
          var = var+tot.marks_obtained
          
        
        return direct_to_template(request,'search_results.html',{'exams':exams,'stud':stud,'total':var,'gtot':gtot,'query' : q})
        
    else: 
      
        return HttpResponse('Please Enter a Valid number')
