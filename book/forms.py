from django import forms 

from .models import Book, AgeGroupCategory

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        age_group = forms.ModelChoiceField(queryset=AgeGroupCategory.objects.all(), empty_label=None)
        fields = ('title', 'author', 'genre', 'language', 'isbn', 'age_group', 'image','description')

        widgets= {
            'title':  forms.TextInput(attrs={
                'placeholder': 'Book Title',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'author':  forms.TextInput(attrs={
                'placeholder': 'Author',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'genre':  forms.TextInput(attrs={
                'placeholder': 'Book Genre',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'language':  forms.TextInput(attrs={
                'placeholder': 'Language',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'isbn':  forms.TextInput(attrs={
                'placeholder': 'ISBN',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'age_group':  forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'description':  forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'image':  forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'})
        }

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        age_group = forms.ModelChoiceField(queryset=AgeGroupCategory.objects.all(), empty_label=None)
        fields = ('title', 'author', 'genre', 'language', 'isbn', 'age_group', 'image','description')

        widgets= {
            'title':  forms.TextInput(attrs={
                'placeholder': 'Book Title',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'author':  forms.TextInput(attrs={
                'placeholder': 'Author',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'genre':  forms.TextInput(attrs={
                'placeholder': 'Book Genre',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'language':  forms.TextInput(attrs={
                'placeholder': 'Language',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'isbn':  forms.TextInput(attrs={
                'placeholder': 'ISBN',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'age_group':  forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'description':  forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'w-full py-4 px-6 rounded-xl border'}),
            'image':  forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'})
        }