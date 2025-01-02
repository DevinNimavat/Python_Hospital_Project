from django.urls import path

from adminapp import views

urlpatterns = [
    path('admin_dashbord/', views.admin_dashbord, name='admin_dashbord'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('show_appointment/',views.show_appointment,name='show_appointment'),
    path('show_doctor/',views.show_doctor,name='show_doctor'),
    path('delete_doctor/<int:id>',views.delete_doctor),
    path('update_doctor/<int:id>',views.update_doctor),
    path('add_staff/',views.add_staff),
    path('show_staff/',views.show_staff,name='show_staff'),
    path('show_patients/',views.show_patients_data),
    path('delete_staff/<int:id>',views.delete_staff),
    path('update_staff/<int:id>',views.update_staff),
    path('delete_appointment/<int:id>',views.delete_appointment),

]
