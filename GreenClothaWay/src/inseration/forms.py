from django import forms

from .models import Inseration


class InserationForm(forms.ModelForm):
    images = forms.ImageField()

    class Meta:
        model = Inseration
        fields = ('title', 'description', 'category', 'subcategory', 'size', 'images',)


class InserationUpdateForm(forms.ModelForm):
    class Meta:
        model = Inseration
        fields = ('title', 'description', 'category', 'subcategory', 'size', 'images',)

    def remove_insertion(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                Inseration.objects.exclude(pk=self.instance.pk).get(email=email)
            except Inseration.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)


class InserationFilterForm(forms.ModelForm):
    class Meta:
        model = Inseration
        fields = ('category', 'subcategory', 'size')