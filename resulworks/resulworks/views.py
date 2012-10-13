# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from result.models import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

def home(request):

    return direct_to_template(request,'home.html',)

def first(request):
    
    return direct_to_template(request,'search_form.html',)

def second(request):
    return direct_to_template(request,'search_form2.html',)

    
def third(request):
    return direct_to_template(request,'search_form.html',)
    #return HttpResponse("Not there yet")

def fourth(request):
    return direct_to_template(request,'search_form.html',)

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
          
        
        return direct_to_template(request,'search_results2.html',{'exams':exams,'stud':stud,'total':var,'gtot':gtot,'query' : q})
        
    else: 
      
        return HttpResponse('Please Enter a Valid number')
def banner(request):
    import settings,glob, random, os.path
    from django.http import HttpResponse
    image_ext = None
    image_data = None
    image_dir = settings.BANNER_DIR
    ext_mimetypes = {
        'jpg': 'image/jpeg',
        'gif': 'image/gif',
        'png': 'image/png', }
    if os.path.isdir(image_dir):
        images = []
        for ext in ext_mimetypes.keys():
            paths = glob.glob(os.path.join(image_dir, '*.' + ext))
            images.extend(paths)
        if len(images) > 0:
            image = random.choice(images)
            image_ext = image.split('.')[-1]
            image_data = open(image, 'rb').read()
    return HttpResponse(image_data, mimetype=ext_mimetypes.get(image_ext))
    
