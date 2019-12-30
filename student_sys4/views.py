from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from student_sys4.forms import StudentForm
from student_sys4.models import Student

from django.views import View


"""
def index( request ):
    students = Student.objects.all( )
    if request.method == 'POST':
        form = StudentForm( request.POST )
        if form.is_valid( ):
            cleaned_data = form.cleaned_data
            student = Student( )
            student.name = cleaned_data['name']
            student.sex = cleaned_data[ 'sex' ]
            student.email = cleaned_data[ 'email' ]
            student.profession = cleaned_data[ 'profession' ]
            student.qq = cleaned_data[ 'qq' ]
            student.phone = cleaned_data[ 'phone' ]
            student.save( )
            return HttpResponseRedirect( reverse( 'index' ) )
    else:
        form = StudentForm( )

    context = { 'students':students , 'form':form , }

    return render( request , 'index.html' , context = context )
"""


"""
#第一次修改后
def index( request ):
    students = Student.get_all( )
    if request.method == 'POST':
        form = StudentForm( request.POST )
        if form.save( ):
            form.save( )
            return HttpResponseRedirect( reverse('index') )
    else:
        form = StudentForm( )

    context = { 'students':students , 'form':form ,}
    return render( request , 'index.html' , context = context )
"""


#第二次修改
def get_context():
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return context


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        context = get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))
        context = get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)




# Create your views here.
