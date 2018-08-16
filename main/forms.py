#_*_ encoding: utf-8 *_*
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = { 'password': forms.PasswordInput(), }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '用户名'
        self.fields['username'].help_text = '请输入用户名'
        self.fields['password'].label = '密  码'
        self.fields['password'].help_text = '请输入密码'
