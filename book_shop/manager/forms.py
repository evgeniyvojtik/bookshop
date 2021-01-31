from django.forms import ModelForm, Textarea, TextInput
from manager.models import Book, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description']
        widgets =   {"title": TextInput(attrs={'class':'form-control'}),
                     'description': Textarea(attrs={"class":'form-control', 'rows': 5, 'cols': 50})}
        help_texts = {'title': "",
                     "description": "введите описание"}

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment', 'author']
