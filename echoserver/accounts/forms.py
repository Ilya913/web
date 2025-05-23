from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User
from django.contrib.auth import update_session_auth_hash


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_."
    )

    email = forms.CharField(
        required=True,
        label="Электронная почта",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    first_name = forms.CharField(
        required=True,
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password'
        }),
        help_text=None
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password'
        }),
        help_text="Введите тот же пароль, что и выше, для проверки"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        # Убираем стандартные валидаторы сложности пароля
        return password1  # просто возвращаем пароль без проверок

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают!")
        return password2

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label = 'Пароль', widget=forms.PasswordInput())


class ChangeProfile(UserChangeForm):
    password = None
    old_password = forms.CharField(
        label="Старый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    new_password2 = forms.CharField(
        label="Подтверждение нового пароля",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    email = forms.CharField(
        label="Электронная почта",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('email', 'first_name')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        old_password = cleaned_data.get("old_password")

        if new_password1 or new_password2 or old_password:
            if not old_password:
                self.add_error('old_password', "Необходимо ввести старый пароль")
            elif not self.instance.check_password(old_password):
                self.add_error('old_password', "Старый пароль введён неверно")
            elif new_password1 != new_password2:
                self.add_error('new_password2', "Пароли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password1')

        if new_password:
            user.set_password(new_password)
            if commit:
                user.save()
                if self.request:
                    update_session_auth_hash(self.request, user)
        elif commit:
            user.save()