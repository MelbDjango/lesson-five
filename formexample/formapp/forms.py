from django import forms

from .models import Person


# class HelloWorldForm(forms.Form):
#     name = forms.CharField(label="Say Hello")
#     awesome = forms.BooleanField(label="Are they awesome?", required=False)

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if not name.lower().startswith('b'):
#             raise forms.ValidationError("Wait a second, %s doesn't start with B!" % name)
#         return name


class HelloWorldForm(forms.ModelForm):
    name = forms.CharField(label="Say Hello")
    awesome = forms.BooleanField(label="Are they awesome?", required=False)

    class Meta:
        model = Person
        fields = ('name', 'awesome')

    def save(self, commit=True):
        """
        This method is unique to ModelForms

        Override the default save method to ensure that people are only
        saved as awesome if their name starts with 'b'
        """
        person = super().save(commit=False)

        if not person.name.lower().startswith('b'):
            person.awesome = False

        if commit:
            person.save()

        return person
