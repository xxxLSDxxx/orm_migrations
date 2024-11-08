from django.urls import path

from school.views import students_list, test_list

urlpatterns = [
    path('', students_list, name='students'),
    path('st/', test_list),
    
]
