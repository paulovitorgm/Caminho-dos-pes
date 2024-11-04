from django.contrib.auth.models import User
from django.forms import CharField, EmailInput, ModelForm, PasswordInput


class UserForm(ModelForm):
    first_name = CharField(label='Nome', max_length=150)
    last_name = CharField(label='Sobrenome', max_length=150)
    email = CharField(
        label='E-mail',
        max_length=254,
        widget=EmailInput(attrs={'autocomplete': 'off'}),
    )
    password = CharField(
        label='Senha',
        max_length=128,
        widget=PasswordInput(attrs={'autocomplete': 'off'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
