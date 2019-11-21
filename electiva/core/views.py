from django.shortcuts import render, HttpResponse
from django.apps import apps
Notice = apps.get_model('notice', 'Notice')
Course = apps.get_model('course', 'Course')

# Create your views here.
def home(request):
    noticias = Notice.objects.all()
    cursos = Course.objects.all()
    return render(request, "core/base.html", {'notices':noticias, 'courses':cursos})
