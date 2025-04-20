from django import forms
from ..models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'photo']
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40})  # Limiting lines of the textarea
        }

    # Customizing the photo field
    photo = forms.ImageField(
        label="Photo: Upload an optional photo for this task",  # Custom label
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        help_text="You can upload a photo to accompany this task (optional)."  # Custom help_text
    )
