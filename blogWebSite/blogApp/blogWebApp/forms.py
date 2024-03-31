from django import forms
from .models import UserProfile, BlogEntry

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
        
class BlogForm(forms.Form):
    class Meta:
        model = BlogEntry
        fields = ['topic_name', 'date_of_creation', 'blog_script', 'image']  # Include 'image' field for image upload
        widgets = {
            'blog_script': forms.Textarea(attrs={'rows': 5})  # Customize the textarea widget if needed
        }
    # topic_name = forms.CharField(max_length=100)
    # date_of_creation = forms.DateField()
    # blog_script = forms.CharField(widget=forms.Textarea)
