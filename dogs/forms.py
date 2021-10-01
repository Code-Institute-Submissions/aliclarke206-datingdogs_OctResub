from django import forms
from .widgets import CustomClearableFileInput
from .models import Dog, Breed


class NewDogForm(forms.ModelForm):

    class Meta:
        model = Dog
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        breeds = Breed.objects.all()
        friendly_names = [(b.id, b.get_friendly_name()) for b in breeds]

        self.fields['breed'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
