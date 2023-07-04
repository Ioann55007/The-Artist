from django.forms import ModelForm

from . models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

