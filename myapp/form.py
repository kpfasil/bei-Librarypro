
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth

def create_profile(self,img,**kwargs):
    Profile.objects.create(
        user=self,
        profile_image=img,
    )
auth.models.User.add_to_class('create_profile', create_profile)

# User Signin
class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

    class Meta:
        model = User
        fields = ['username','password']

class BookForm(forms.ModelForm):
    class Meta : 
        model=BookModel
        fields=['book_name','description','author','image'] 

        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Book Name'}),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Description'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Author Name'}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'Enter Book Name'}),
        }

class SignupForm(UserCreationForm):
    profile_image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Upload user picture'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))


    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.username=self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1=self.cleaned_data['password1']
        user.password2=self.cleaned_data['password2']

        # user has to be saved to add profile
        user.save()
        img = self.cleaned_data.get('profile_image')
        user.create_profile(img)
        user.profile.save() 
        

        if commit:
            user.save()