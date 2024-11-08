from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    students = Student.objects.all()
    template = 'school/students_list.html'
    ordering = 'group'
    context = {'object_list': students.order_by(ordering)}
    print(students)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    

    return render(request, template, context)
def test_list(request):
    Teachers= Teacher.objects.all()
    # template = 'school/students_list.html'
    template = 'test.html'
    context = {'Teachers': Teachers}
    print(Teachers)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

