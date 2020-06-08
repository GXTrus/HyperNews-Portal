from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    text = forms.CharField(label='Text', max_length=2000)


class NewsSearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100)
