from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post
from django.core.validators import RegexValidator


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image', 'status',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please fill like the title'}),
        }

    featured_image = forms.ImageField(required=True)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
    first_name = forms.CharField(required=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Only English letters are allowed.',
            code='invalid_input'
        )
    ])
    last_name = forms.CharField(required=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Only English letters are allowed.',
            code='invalid_input'
        )
    ])
    email = forms.EmailField(required=True)