from result2.models import *

from django.contrib import admin

class subdisp(admin.ModelAdmin):
    list_display = ('subject_id','subject')
class studsp(admin.ModelAdmin):
    list_display = ('student_id','student_name','student_dep')
class grade_disp(admin.ModelAdmin):
    list_display = ('student','subject','student_dep','maximum_marks','marks_obtained')

admin.site.register(Student,studsp)
admin.site.register(Subject,subdisp)
admin.site.register(StudentDep)
admin.site.register(Exam,grade_disp)
