from django import forms
from django.contrib.auth.models import User

class ResetPasswordForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu mới")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Xác nhận mật khẩu")

    class Meta:
        model = User
        fields = ['new_password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Mật khẩu và xác nhận mật khẩu không khớp.")
        return cleaned_data
