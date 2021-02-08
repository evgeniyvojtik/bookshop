from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.forms import ModelForm, Textarea, TextInput, forms, CharField, PasswordInput
from manager.models import Book, Comment


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass
    username = UsernameField(widget=TextInput(attrs={'class': "form-control", 'autofocus': True}))
    password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),

    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
    )


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description']
        widgets = {"title": TextInput(attrs={'class': 'form-control'}),
                   'description': Textarea(attrs={"class": 'form-control', 'rows': 5, 'cols': 50})}
        help_texts = {'title': "",
                      "description": "введите описание"}


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
