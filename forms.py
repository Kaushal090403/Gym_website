from django import forms
from .models import Member, Trainer, Class, Membership

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
