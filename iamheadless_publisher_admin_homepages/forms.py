from django import forms
from django.forms import formset_factory


class HomepageContentForm(forms.Form):
    language = forms.CharField(initial='', max_length=255, widget=forms.widgets.HiddenInput())
    title = forms.CharField(initial='', max_length=255)
    slug = forms.SlugField(initial='', max_length=255)
    content = forms.CharField(widget=forms.widgets.Textarea())
    seo_keywords = forms.CharField(max_length=160, initial='', required=False)
    seo_description = forms.CharField(max_length=160, initial='', required=False)


HomepageContentFormSet = formset_factory(HomepageContentForm, extra=0)


class HomepageForm(forms.Form):
    pass
