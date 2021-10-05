from django import forms
from .models import Profile


messages = {
    "required": "این فیلد نمیتواند خالی باشد",
    "invalid": "لطفا فیلد را به درستی پر کنید",
    "max_length": "طول رشته بیش از حد است",
    "min_length": "طول رشته کم تر از حد مجاز است",
}


class UserLoginForm(forms.Form):
    username = forms.CharField(
        error_messages=messages,
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "your username"}),
    )
    password = forms.CharField(
        error_messages=messages,
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={"placeholder": "your password"}),
    )


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        error_messages=messages,
        min_length=3,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "your username"}),
    )
    password = forms.CharField(
        error_messages=messages,
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={"placeholder": "your password"}),
    )
    email = forms.EmailField(
        error_messages=messages,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )



class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Profile
        exclude = ('user',)


class PhoneLoginForm(forms.Form):
    phone = forms.IntegerField()