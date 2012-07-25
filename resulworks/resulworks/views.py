# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from result.models import *
from django.conf import settings
from django.views.generic.simple import direct_to_template


def search_result(request):
    
    return direct_to_template(request,'search_form.html',)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        stud = Student.objects.filter(student_id=q)
        var = 0
        exams = Exam.objects.filter(student_id=q)
        for tot in exams:
          var = var+tot.marks_obtained
        
        return direct_to_template(request,'search_results.html',{'exams':exams,'stud':stud,'total':var,'query' : q})
        
    else: 
      
        return HttpResponse('Please Enter a Valid number')
