
from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES =[
#         (NATION_A,'한국'),
#         (NATION_B,'중국'),
#         (NATION_C,'일본'),
#         ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.forms.ChoiceField( choices=NATIONS_CHOICES)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder':'Enter the title',
                'maxlength':10,
            }
        )

    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages={
            'required':'내용 입력하라고오.....',
        }
    )
    class Meta:
        model = Article #어떤 모델을 기반으로 할지
        fields = '__all__' # 어떤 모델필드 중 어떤것을 출력할지 
        # excluse = ('title',)