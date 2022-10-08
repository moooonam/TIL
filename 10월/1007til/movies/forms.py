from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Title',
                'maxlength':20,
            }
        )
    )
    audience = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Audience',
            }
        )
    )
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder':'연도-월-일',
                'type':'date',
            }
        )
    )
    genres = [('코미디','코미디'), ('공포','공포'), ('로맨스','로맨스')]
    genre = forms.ChoiceField(
        choices=genres, 
        widget=forms.Select(
            attrs={
                'placeholder':'Genre',
                'maxlength':30,
            }
        )
    )

    score = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Score',
                'type':'number',
                'step':0.5,
                'min':0,
                'max':5,
            }
        )
    )
    poster_url = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Poster url',

            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Description',
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'