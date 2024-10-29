from django.forms import ModelForm

from apps.anamnese.models import AnamneseModel


class AnamneseForm(ModelForm):
    class Meta:
        model = AnamneseModel
        fields = '__all__'
