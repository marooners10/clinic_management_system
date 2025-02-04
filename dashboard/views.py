from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Patient, Medicine
from .forms import PatientForm, MedicineForm
from django.contrib.auth.models import User
from django.contrib import messages 
from django.shortcuts import get_object_or_404


# Create your views here.

@login_required(login_url='user-login')
def index(request):# for making request from staff
    medicines = Medicine.objects.all()
    medicines_count = medicines.count()
    patients = Patient.objects.all()
    patients_count = patients.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = MedicineForm()
    context={
        'medicines': medicines,
        'form': form,
        'patients': patients,
        'patients_count' : patients_count,
        'medicines_count' : medicines_count,
        'workers_count' : workers_count
    }
    return render(request, 'dashboard/index.html', context) #parameter and name of template


@login_required(login_url='user-login')
def staff(request):#for staff
    workers = User.objects.all()
    workers_count = workers.count()# Counts the total users
    medicines_count = Medicine.objects.all().count()
    patients_count = Patient.objects.all().count()
    context={
        'workers': workers,
        'workers_count': workers_count,
        'medicines_count': medicines_count,
        'patients_count': patients_count
    }
    return render(request, 'dashboard/staff.html', context) #parameter and name of template


@login_required(login_url='user-login')
def staff_detail(request, pk): #for staff's detail
    workers = User.objects.get(id=pk)
    context ={
        'workers': workers
    } 
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def Patient_view(request):
    items = Patient.objects.all()#using Object Relational Mapping
    patients_count = Patient.objects.count() # of total Patient
    workers_count = User.objects.all().count()
    medicines_count = Medicine.objects.all().count()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            Patient_name = form.cleaned_data.get('name')#grabbing the name from models
            messages.success(request, f'{Patient_name} has been added.')
            return redirect('dashboard-patient')
        else:
            print("Form errors:", form.errors)
    else:
        form = PatientForm()
    context={
        'items': items,
        'form': form,
        'patients_count' : patients_count,
        'workers_count': workers_count,
        'medicines_count': medicines_count
    }
    return render(request, 'dashboard/patient.html', context) #parameter and name of template



@login_required(login_url='user-login')
def Patient_delete(request, pk):  # for deleting Patient
    item = get_object_or_404(Patient, id=pk)  # ✅ This prevents the DoesNotExist error
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-patient')  # Ensure this matches the URL name
    return render(request, 'dashboard/patient_delete.html', {'item': item})  # Pass the object to template



@login_required(login_url='user-login')
def Patient_update(request, pk): #for editing particular Patient
    item = Patient.objects.get(id=pk)
    if request.method=='POST':
        form = PatientForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-patient')
    else:
        form = PatientForm(instance=item)
    context={
        'form': form
    }
    return render (request, 'dashboard/patient_update.html', context)



@login_required(login_url='user-login')
def Medicine_view(request):
    medicines = Medicine.objects.all()
    medicines_count = medicines.count()#for total medicines
    workers_count = User.objects.all().count()
    patients_count = Patient.objects.all().count()
    context={
        'medicines': medicines,
        'workers_count': workers_count,
        'medicines_count': medicines_count,
        'patients_count' : patients_count
    }
    return render(request, 'dashboard/medicine.html', context)



@login_required(login_url='user-login')
def Medicine_delete(request, pk):  # for deleting Medicine
    item = get_object_or_404(Medicine, id=pk)  # ✅ This prevents the DoesNotExist error
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-medicine')  # Ensure this matches the URL name
    return render(request, 'dashboard/medicine_delete.html', {'item': item})  # Pass the object to template



@login_required(login_url='user-login')
def Medicine_update(request, pk): #for editing particular Medicine
    item = Medicine.objects.get(id=pk)
    if request.method=='POST':
        form = MedicineForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-medicine')
    else:
        form = MedicineForm(instance=item)
    context={
        'form': form
    }
    return render (request, 'dashboard/medicine_update.html', context)