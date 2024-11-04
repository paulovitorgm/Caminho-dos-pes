from django.contrib.auth.models import User
from django.forms import CharField, EmailInput, ModelForm


class EditarUserForm(ModelForm):
    first_name = CharField(label='Nome', max_length=150)
    last_name = CharField(label='Sobrenome', max_length=150)
    email = CharField(
        label='E-mail',
        max_length=254,
        widget=EmailInput(attrs={'autocomplete': 'off'}),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
