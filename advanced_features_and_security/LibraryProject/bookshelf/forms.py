from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

        
# ✅ Example of a Secure Form for Handling User Input Safely
class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )

    # Optional: Clean and sanitize user input explicitly
    def clean_query(self):
        data = self.cleaned_data['query']
        # Further sanitization or restrictions can be applied if needed
        return data