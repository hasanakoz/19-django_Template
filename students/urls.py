from django.urls import path
from .views import home, student_list, student_add, student_update, student_detail, student_delete


urlpatterns = [
    path('', home, name = 'home' ),
    path('student_list/', student_list, name = 'student_list' ),
    path('student_add/', student_add, name = 'student_add' ),
    path('student_update/<int:id>', student_update, name = 'student_update' ),
    path('student_detail/<int:id>', student_detail, name = 'student_detail' ),
    path('student_delete/<int:id>', student_delete, name = 'student_delete' ),
]