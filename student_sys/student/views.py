from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student

# Create your views here.
# 封装成类
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

class IndexView(View):
    template_name = 'student/index.html'

    def get_context(self):
        students = Student.get_all()
        context = {}
        context['students'] = students
        return context

    # 处理get请求
    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context['form'] = form
        return render(request, self.template_name, context)

    # 处理post请求
    def post(self, request):
        form =  StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context['form'] = form
        return render(request, self.template_name, context)
