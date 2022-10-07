from django import forms
from .models import Movie

genre_choices = [('코미디', '코미디'), ('공포', '공포'), ('로맨스', '로맨스')]

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Title',
            'class': 'form-control'},
        )
    )
    audience = forms.IntegerField(
        widget = forms.NumberInput(
            attrs = {'placeholder': 'Audience',
            'class': 'form-control'},
        )
    )
    release_date = forms.DateField(
        widget = forms.DateInput(
            attrs = {'placeholder': 'Release_date', 'class': 'form-control'},
        )
    )
    genre = forms.ChoiceField(
        choices=genre_choices,
        widget = forms.Select(
            attrs = {'class': 'form-control'}
        )
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Score', 'step':0.5, 'min':0, 'max':5,
            'class': 'form-control'},
        )
    )

    poster_url = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Poster_url', 'class': 'form-control'},
        )
    )
    description = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Description', 'class': 'form-control'},
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'