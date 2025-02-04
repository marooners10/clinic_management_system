from django import forms
from .models import Patient, Medicine

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  # Include all model fields
        # OR explicitly specify existing fields:
        # fields = ['name', 'age', 'address']  # Replace with actual fields from the Patient model
        

# class MedicineForm(forms.ModelForm):
#     class Meta:
#         model = Medicine
#         #fields = '__all__'  # Include all model fields
#         # OR explicitly specify existing fields:
#         fields = ['patient', 'name', 'category', 'medicine_quantity', 'staff',]  # Replace with actual fields from the Medicine model
        

class MedicineForm(forms.ModelForm):
    patient_category = forms.ChoiceField(
        required=False,  # Not required since it's just for display
        label="Patient Category",
        choices=[] + [(category, category) for category in ['New Patient', 'Follow-Up Patient', 'Emergency Patient', 'Preventive Care Patient']]  # Add your categories here
    )

    class Meta:
        model = Medicine
        fields = ['patient', 'patient_category', 'medicine_name', 'medicine_category', 'medicine_quantity', 'staff']

    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.patient:
            # Pre-populate the patient category field with the patient's category
            self.fields['patient_category'].initial = getattr(self.instance.patient, 'category', '')

        # Optionally, if the user can choose a category from a model or predefined set, you can populate the choices dynamically.
