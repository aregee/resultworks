

#Resultworks

============

A Django based web app using MySQL back end for rendering college grade report.
Providing a webbased interface for updating database of students and adding grade report.
Using Django's Admin app,teachers or HOD's would be able to update student records for each examination directly.

## Table Of Contents

1. Author
2. Requirements
3. Deployment Instructions 
4. Useful Links

### 1. Author 

Authro: Aregee <rahul.nbg@gmail.com>
Blog: <http://rahulgaur.info>

This file is part of ResultWorks.

    ResultWorks is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ResultWorks is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ResultWorks.If not, see http://www.gnu.org/licenses.

### 2.Requirements 
     Django==1.4
     MySQL-python==1.2.3
     MySQL
     

### 3.Deployment 
   For Heroku deployment do the following :
   Make a new Dir for ResultWorks 

   	$ mkdir resultworks && cd resultworks

   Create a Virtualenv:
   
   	$ virtualenv venv --distribute
   	New python executable in venv/bin/python
   	Installing distribute...............done.
   	Installing pip...............done.

   To activate Environment You need to Source it:
   

   	$ source venv/bin/activate

   Install dependencies with pip

    $ pip install Django psycopg2 dj-database-url
    Downloading/unpacking Django
    Downloading Django-1.4.tar.gz (7.6Mb): 7.6Mb downloaded
    Running setup.py egg_info for package Django
    ......................................
    .....................................
    ................................

   Now add this upstream repo
    
    $ git remote add upstream -m master git@github.com:aregee/resultworks.git .
    $ git pull -s recursive -X theirs upstream master

Now Push to Heroku :
See Getting Started With Django on Heroku: <https://devcenter.heroku.com/articles/django>
You will have to change the Database in settings.py to make it work with Postgre SQL if you are using MySQL or You have a mysql server configured use it.
I have also tired hosting Django Apps on Openshift and I Will create a seprate fork for that ..
To run the app locally, cd into the dir and do 
   ./manage.py runserver
    
### 4. Useful Links:
Django Documentation <https://docs.djangoproject.com/en/1.4>
    
Get Django :
Download <https://www.djangoproject.com/download/1.4.1/tarball/>    	
Or
	git clone https://github.com/django/django.git	
	
Hands on YouTube : <http://youtu.be/ko4yV8rrHR8>

OpenShift : <http://resworks-rahulgaur.rhcloud.com> , <https://resworks-rahulgaur.rhcloud.com/admin>
