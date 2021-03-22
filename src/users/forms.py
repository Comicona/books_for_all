from django.contrib.auth import forms as auth_forms, models as auth_models
from django import forms
from users import models

class UserProfileExtForm(forms.ModelForm):
    class Meta:
        model = models.ExtUserData
        fields = ('phone', 'country', 'city', 'post_index', 'address1' ,'address2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = ('first_name', 'last_name', 'email')