from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    # author = forms.CharField(label='author', max_length=100)
    # ISBN =  forms.CharField(label='ISBN', max_length=13)