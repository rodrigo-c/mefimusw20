from dal import autocomplete
from django import forms
from core.models import Mix, MyUser
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MixForm(forms.ModelForm):
    class Meta:
        model = Mix
        # fields = ('title', 'text', 'cover_image', 'back_image', 'tags', 'bg_color', 'tx_color')
        fields = ('title', 'text', 'cover_image', 'back_image', 'tags')
        widgets = {
            'tags': autocomplete.ModelSelect2Multiple(url='tag-autocomplete')
        }


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", 'platform', 'mefi_handle')
        field_classes = {'username': UsernameField}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields.pop('password2')
    password2 = None


class SigninForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class CommentForm(forms.Form):
    text = forms.CharField()
    objectid = forms.CharField()
    objectclass = forms.CharField()
