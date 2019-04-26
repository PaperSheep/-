from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    # 使用models.py文件里自己封装的方法get_all()
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # 这里的写法可被下面那句代替
            # cleaned_data = form.cleaned_data
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()
            form.save()
            # 全部成功然后返回主页
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {}
    context['words'] = 'Word!'
    context['students'] = students
    context['form'] = form
    return render(request, 'student/index.html', context)

