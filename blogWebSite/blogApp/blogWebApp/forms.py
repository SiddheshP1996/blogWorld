from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
        
class BlogForm(forms.Form):
    topic_name = forms.CharField(max_length=100)
    date_of_creation = forms.DateField()
    blog_script = forms.CharField(widget=forms.Textarea)
