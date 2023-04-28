# -*- coding: utf-8 -*-
# time:2023/4/25 7:50
# file forms.py
# outhor:czy
# email:1060324818@qq.com
from django import forms
from django.contrib.auth.models import User
from .models import Category, Page, UserProfile

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class CategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=128,help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):

    title = forms.CharField(max_length=128,help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):

        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data


""" {% csrf_token %} 必须要有这一行，否则报错"""