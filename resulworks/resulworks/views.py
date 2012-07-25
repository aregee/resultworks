# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from result.models import *
from django.conf import settings


def search_result(request):
    resp = {}
    resp['MEDIA_URL'] = settings.MEDIA_URL
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        
        stud = Student.objects.filter(student_id=q)
        var = 0
        exams = Exam.objects.filter(student_id=q)
        for tot in exams:
          var = var+tot.marks_obtained
        
        return render_to_response('search_results.html',{'exams':exams,'stud':stud,'total':var,'query' : q})
        
    else: 
      
        return HttpResponse('Please Enter a Valid number')
