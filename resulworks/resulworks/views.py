# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from result.models import *


def search_result(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        stud = Student.objects.filter(student_id=q)
        
        exams = Exam.objects.filter(student_id=q)
        return render_to_response('search_results.html',{'exams':exams,'stud':stud,'query' : q})
        
    else: 
      
        return HttpResponse('Please Enter a Valid number')
