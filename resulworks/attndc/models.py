from django.db import models
from result.models import Student


#DB to hold daily attendance 
class Attnd(models.Model):
    stud = models.ForeignKey(Student)
    
    def __unicode__(self):
        return stud.Student.stu

class choice(models.Model):
    stu_name = models.ForeignKey(Attnd)
    CHOICE = (
        (u'P',u'Present'),
        (u'A',u'Absent'),
        )
    status = models.CharField(max_length=100,choices=CHOICE)
    #atcount = models.IntegerField()
    date = models.DateTimeField('Date')

    def __unicode__(self):
        return self.status




    
