from django import forms
from django.core import validators


def capital(value):
    if not('A' <= value[0] <= 'Z'):
        raise forms.ValidationError("Username First Letter must be Capital")


class Register(forms.Form):
    # firstname = forms.CharField(widget=forms.Textarea(attrs={'row':1}))
    firstname = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput, label='Last_Name')
    age = forms.IntegerField(min_value=18, max_value=45)
    dob = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    # yr = ['2017', '2018', '2019', '2020']
    # dob = forms.DateField(widget=forms.SelectDateWidget(years = yr))
    lst = [('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')]
    gender = forms.ChoiceField(choices=lst)
    # gender = forms.MultipleChoiceField(choices=lst)
    # gender = forms.ChoiceField(widget=forms.RadioSelect, choices = lst)
    # gender = forms.MultipleChoiceField(widget=forms.CheckBoxSelectMultiple, choices = lst)
    email = forms.EmailField()
    phone = forms.IntegerField()
    # username = forms.CharField(min_length=4, max_length=10, required=True,initial='USERNAME@1')
    username = forms.CharField(min_length=4, max_length=10, required=True, initial='User@1', validators=[capital])
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)
    # images = forms.ImageField()
    file = forms.FileField()

    def clean(self):
        ph = self.cleaned_data['phone']
        if len(str(ph)) != 10:
            raise forms.ValidationError("Phone must be 10 digits")
        pas = self.cleaned_data['password']
        pas2 = self.cleaned_data['confirmPassword']
        if pas != pas2:
            raise forms.ValidationError("Password Mismatch")

        """
        user = self.cleaned_data['username']
        if not('A' <= user[0] <= 'Z'):
            raise forms.ValidationError("Username First Letter must be Capital")
        """

