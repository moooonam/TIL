from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'
        # exclude = ('author',)

class CommentForm(forms.ModelForm):
    #선택을 위한 input이 체크박스(기본값) 이 아니라 셀렉트로 바꾸고 싶을때
    PICKS = [
        (False, "RED TEAM"),
        (True, "BLUE TEAM"),
    ]
    pick = forms.ChoiceField(choices=PICKS, widget=forms.Select())
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('question',)