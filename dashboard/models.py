from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
CATEGORY = (
    ('New Patient', 'New Patient'),
    ('Follow-Up Patient', 'Follow-Up Patient'),
    ('Emergency Patient', 'Emergency Patient'),
    ('Preventive Care Patient', 'Preventive Care Patient'),
)#tuple of tuple


# Patient Model
class Patient(models.Model): #inherits from models package
    name = models.CharField(max_length=100, blank=True, null=False)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length= 30, choices=CATEGORY, null=True)
    problem = models.CharField(max_length= 30, null=True)
    
    #change the name of the model
    class Meta:
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return f'{self.name}' #name and problem of Patient
    

#category for medicine
CATEGORY1 = (
    ('Oral', 'Oral'),
    ('Topical', 'Topical'),
    ('Injectable', 'Injectable'),
    ('Inhalable', 'Inhalable'),
    ('Transdermal', 'Transdermal'),
)#tuple of tuple

# Medicine Model
class Medicine(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    medicine_category = models.CharField(max_length= 30, choices=CATEGORY1, null=True)
    medicine_name = models.CharField(max_length=100, blank=True, null=False)
    medicine_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add= True)
    
    #change the name of the model
    class Meta:
        verbose_name_plural = 'Medicines'
    
    def __str__(self):
        return f'{self.patient} Issued by {self.staff.username if self.staff else "Unknown"}'



