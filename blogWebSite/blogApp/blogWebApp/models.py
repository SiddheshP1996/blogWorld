import pytz
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class ContactInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='Contact Person')
    email = models.EmailField(max_length=50, verbose_name='Contact Email')
    contact = models.CharField(max_length=15, verbose_name='Contact Number')
    message = models.TextField(max_length=200, verbose_name='Suggestions')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created At')
    
    def __str__(self):
        return self.name

class BlogEntry(models.Model):
    topic_name = models.CharField(max_length=40, verbose_name='Topic Name')
    categories = models.ManyToManyField('BlogCategory', related_name='blog_entries', verbose_name='Categories')
    date_of_creation = models.DateField(verbose_name='Date of Creation',  default=timezone.now)
    last_updated_at = models.DateTimeField(verbose_name='Last Updated At', auto_now=True)
    blog_script = models.TextField(verbose_name='Blog Script')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_entries', default=1)
    image = models.ImageField(upload_to='blog_images/', verbose_name=_('Image'), null=True, blank=True)

    def __str__(self):
        return self.topic_name
    
    def formatted_last_updated_at(self):
        # Convert last_updated_at to Indian Standard Time (IST)
        tz = pytz.timezone('Asia/Kolkata')
        localized_time = timezone.localtime(self.last_updated_at, tz)
        return localized_time.strftime('%Y-%m-%d %H:%M:%S')
    
    class Meta:
        verbose_name = _('Blog Entry')
        verbose_name_plural = _('Blog Entries')
       
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    bio = models.TextField(blank=True, null=True, verbose_name='Bio')
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name='Location')

    def __str__(self):
        return f'{self.user.username} Profile'

class BlogCategory(models.Model):
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('food', 'Food'),
        ('fitness', 'Fitness'),
        ('travel', 'Travel'),
        ('fashion', 'Fashion'),
        ('finance', 'Finance'),
        ('entertainment', 'Entertainment'),
        ('education', 'Education'),
        ('parenting', 'Parenting'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Category Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name
    
    def get_external_link(self):
        for choice in self.CATEGORY_CHOICES:
            if choice[0] == self.name:
                return choice[2]
        return None