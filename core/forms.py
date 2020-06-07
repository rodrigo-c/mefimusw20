from dal import autocomplete
from django import forms
from core.models import Mix, MyUser
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MixForm(forms.ModelForm):
    class Meta:
        model = Mix
        fields = ('title', 'text', 'link', 'cover_image', 'back_image', 'tags')
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(url='tag-autocomplete')
        }


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", 'platform', 'mefi_handle')
        field_classes = {'username': UsernameField}

    birthdate = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y',)

    )
    policies = forms.BooleanField(widget=forms.CheckboxInput, initial=False, required=True)

class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())