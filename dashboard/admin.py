from django.contrib import admin
from .models import Patient, Medicine  # Import your models
from user.models import Profile



# Change the title of your admin pannel
admin.site.site_header = 'NepClinic Dashboard'


# Display in table format in admin pannel for Patient
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name')
    list_filter = ['category']
    

# Register models
admin.site.register(Patient)
admin.site.register(Medicine)
admin.site.register(Profile)