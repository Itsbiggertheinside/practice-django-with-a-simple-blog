from django import forms
from .models import Account
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Kullanıcı adı: ')
    password = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Parola: ')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adı veya parolanızı yanlış girdiniz.')

        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=35, label='Kullanıcı adı: ')
    email = forms.EmailField(label='Email adresi: ')
    password1 = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Parola: ')
    password2 = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Parola tekrarı: ')

    class Meta:
        model = Account
        fields = ('username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parolalar eşleşmiyor!')

        return password2

class UpdateForm(forms.ModelForm):

        username = forms.CharField(label='Kullanıcı adı: ')
        pic = forms.FileField(label='Profil fotoğrafı: ')
        city = forms.CharField(label='Bulunduğu şehir: ')
        webpage = forms.CharField(label='Web siten: ')
        three_word = forms.CharField(label='Kendini üç kelimeyle tanıt: ')
        about = forms.CharField(widget=forms.Textarea, label='Kendin hakkında: ')

        class Meta:
            model = Account
            fields = ('username', 'pic', 'city', 'webpage', 'three_word', 'about')