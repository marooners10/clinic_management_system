from django.urls import path
from . import views #import views file from current folder



urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'), #importing index function from views,py
    path('staff/', views.staff, name='dashboard-staff'), #importing staff function from views.py
    path('patient/', views.Patient_view, name='dashboard-patient'), #importing staff function from views.py
    path('patient/delete/<int:pk>', views.Patient_delete, name='dashboard-patient-delete'), #importing patient-delete function from views.py
    path('patient/update/<int:pk>', views.Patient_update, name='dashboard-patient-update'), #importing patient-update function from views.py
    path('staff/detail/<int:pk>', views.staff_detail, name='dashboard-staff-detail'),#importing staff_detail function
    path('medicine/', views.Medicine_view, name='dashboard-medicine'), #importing staff function from views.py
    path('medicine/delete/<int:pk>', views.Medicine_delete, name='dashboard-medicine-delete'), #importing medicine-delete function from views.py
    path('medicine/update/<int:pk>', views.Medicine_update, name='dashboard-medicine-update'), #importing medicine-update function from views.py
]
