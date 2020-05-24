from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account

def decorator_email_field(clazz):
    # bad: using internal from django, doesnt work with local email field only
    clazz.base_fields['email'] = forms.EmailField(max_length=60, label='Email', help_text='Required. Add a valid email address')
    return clazz


@decorator_email_field
class SignUpForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name', 'street', 'housenumber', 'plz', 'city',
                  'country', 'password1', 'password2')


@decorator_email_field
class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid login')


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'street', 'housenumber', 'plz', 'city',
                  'country')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)
