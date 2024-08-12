import requests
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail
from django.contrib import messages
from blogWebApp.models import ContactInfo, BlogEntry, UserProfile, BlogCategory
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, BlogForm

from newsapi import NewsApiClient

def home(request):
    if request.method == 'GET':
        blog_entries = BlogEntry.objects.all().select_related('author')
        return render(request, 'index.html', {'blog_entries': blog_entries})
    else:
        return render(request, 'methodnotallowed.html')
        # return HttpResponse("Method not allowed", status=405)

def register(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['fullname']
        username = request.POST['username']
        userpassword = request.POST['userpassword']
        confirmpassword = request.POST['confirmpassword']
        if name == "" or username == "" or userpassword == "" or confirmpassword == "":
            context['errormessage'] = "Fields Cannot be Empty"
            return render(request, 'register.html', context)
        elif userpassword != confirmpassword:
            context['errormessage'] = "Enter Same Password for both inputs"
            return render(request, 'register.html', context)
        else:
            try:
                u = User.objects.create(username = username, email = username, first_name = name)
                u.set_password(userpassword)
                u.save()
                context['success'] = "User Created Successfully !"
                return render(request, 'register.html', context)
            except Exception:
                context['errormessage'] = "User with same username already exists."
                return render(request, 'register.html', context)
    else:
        return render(request, 'register.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        userpassword = request.POST['userpassword']
        if username == "" or userpassword == "":
            context['errormessage'] = "Fields Cannot be Empty"
            return render(request, 'login.html', context)
        else:
            user = authenticate(username = username, password = userpassword)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                context['errormessage'] = "Invalid Username or Password"
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)
    
def reset_password(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        newpassword = request.POST['newpassword']
        confirmnewpassword = request.POST['confirmnewpassword']
        if username == "" or newpassword == "" or confirmnewpassword == "":
            context['errormessage'] = "Fields Cannot be Empty"
            return render(request, 'password_reset.html', context)
        elif newpassword != confirmnewpassword:
            context['errormessage'] = "Enter Same Password for both inputs"
            return render(request, 'password_reset.html', context)
        else:
            try:
                u = User.objects.get(username = username)
                u.set_password(confirmnewpassword)
                u.save()
                context['success'] = "Password Updated Successfully !!"
                return render(request, 'password_reset.html', context)
            except Exception:
                context['errormessage'] = "Enter Same Password for both inputs"
                return render(request, 'password_reset.html', context)
    else:
        return render(request, 'password_reset.html', context)

def user_logout(request):
    logout(request)
    return redirect('/home')

def about(request):
    return render(request, 'about.html')

def user_profile(request):
    if request.user.is_authenticated:
        # Retrieve or create the UserProfile object for the current user
        user_profile, created = UserProfile.objects.get_or_create(user = request.user)
        
        # Fetch the user's blog entries
        user_blogs = BlogEntry.objects.filter(author=request.user)
        
        # Fetch other relevant user data (add more as needed)
        name = request.user.first_name
        email = request.user.email
        profile_image = user_profile.image if user_profile.image else None

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                # Fetch the updated user profile after saving the form
                user_profile = form.instance
                # Update the profile_image variable with the newly uploaded image
                profile_image = user_profile.image if user_profile.image else None
        else:
            form = UserProfileForm(instance=user_profile)
            
        # Now that all variables are defined, they can be added to the context
        context = {
            'form': form,
            'name': name,
            'email': email,
            'user_profile': user_profile,
            'user_blogs': user_blogs,
            'profile_image': profile_image
            }

        return render(request, 'user_profile.html', context)
    else:
        return redirect('user-login')  # Redirect to your login URL


def blog_category(request):
    api = NewsApiClient(api_key='424c7dabac204adab6e34bf9968a5d65')
    api.get_sources()
    # News API endpoint for top headlines
    api_url = 'https://newsapi.org/v2/top-headlines'
    api_key = '424c7dabac204adab6e34bf9968a5d65'  # Replace with your News API key

    # Define the categories manually as the News API does not have an explicit category endpoint
    categories = [
        {'name': 'Business', 'description': 'Stay updated with business news, trends, and market analysis.', 'endpoint': 'business'},
        {'name': 'Entertainment', 'description': 'Get the latest entertainment news, celebrity gossip, and more.', 'endpoint': 'entertainment'},
        {'name': 'Health', 'description': 'Read about health trends, medical news, and wellness tips.', 'endpoint': 'health'},
        {'name': 'Science', 'description': 'Discover the latest in scientific research and discoveries.', 'endpoint': 'science'},
        {'name': 'Sports', 'description': 'Follow sports news, scores, and updates from around the world.', 'endpoint': 'sports'},
        {'name': 'Technology', 'description': 'Explore tech news, reviews, and innovations in the tech world.', 'endpoint': 'technology'},
    ]

    # Iterate over the categories to fetch articles for each
    for category in categories:
        params = {
            'category': category['endpoint'],
            'country': 'us',  # You can change the country as needed
            'apiKey': api_key
        }
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            articles = response.json().get('articles', [])
            # Store the first article link as the "Read more" link for simplicity
            category['link'] = articles[0]['url'] if articles else '#'
        except requests.exceptions.RequestException as e:
            category['link'] = '#'
            print(f"Error fetching articles for {category['name']}: {e}")

    context = {
        'categories': categories
    }

    return render(request, 'blog_category.html', context)

def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Handle form submission
            form = BlogForm(request.POST)
            if form.is_valid():
                # Process the form data
                # Save the blog entry, etc.
                messages.success(request, 'Blog created successfully!')
                return redirect('home')  # Redirect to home page or wherever appropriate after successful blog creation
            else:
                # Form is invalid, display error message
                messages.error(request, 'Form is not valid. Please correct the errors.')
        else:
            # Display empty form for creating a new blog entry
            form = BlogForm()
        return render(request, 'create_blog.html', {'form': form})
    else:
        messages.error(request, "You need to log in to create a blog.")
        return redirect('user-login')

def edit_blog(request, blog_id):
    if request.user.is_authenticated:
        blog_entry = get_object_or_404(BlogEntry, id=blog_id)
        # Check if the current user is the author of the blog entry
        if blog_entry.author == request.user:
            # Render the edit_blog.html template with the blog entry
            return render(request, 'edit_blog.html', {'blog_entry': blog_entry})
        else:
            # Return an unauthorized error if the current user is not the author
            return render(request, 'unauthorized.html')
            # return HttpResponse('Unauthorized', status=401)
    else:
        messages.error(request, "You need to log in to create a blog.")
        return render(request, 'unauthorized.html')
        # return HttpResponse('Unauthorized', status=401)


def submit_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':        
            # Fetching current user's full name and using it as the username for the blog entry
            current_user = request.user        
            # Assign the current user directly to the author field
            author = current_user if current_user.is_authenticated else None
            
            topic_name = request.POST.get('topicname')
            files_to_attach = request.FILES.getlist('filestoattach')
            date_of_creation = request.POST.get('dateofcreation')
            blog_script = request.POST.get('blogscript')  
            
            # Process the form data here
            # For example, save it to a database model
            blog_entry = BlogEntry(topic_name=topic_name, date_of_creation=date_of_creation, blog_script=blog_script, author=author)
            blog_entry.save()

            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        else:
            # Return an error response if the request method is not POST
            return JsonResponse({'error': 'Invalid request method'}, status=400)
    else:
        messages.error(request, "You need to log in to create a blog.")
        return redirect('user-login')


def update_blog(request, blog_id):  # Add blog_id parameter
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Fetch the blog entry using the blog_id
            blog_entry = get_object_or_404(BlogEntry, id=blog_id)
            
            # Check if the current user is the author of the blog entry
            if blog_entry.author == request.user:
                # Update the fields of the blog entry based on the form data
                blog_entry.topic_name = request.POST.get('topicname')
                blog_entry.date_of_creation = request.POST.get('dateofcreation')
                blog_entry.blog_script = request.POST.get('blogscript')
                
                # Save the updated blog entry
                blog_entry.save()

                # Redirect to the home page or any other appropriate page
                return redirect('blog-home')
            else:
                # Return unauthorized error if the current user is not the author
                # return HttpResponse("Unauthorized", status=401)
                return render(request, 'unauthorized.html')
        else:
            # Handle the case where the request method is not POST
            # return HttpResponse("Method not allowed", status=405)
            return render(request, 'methodnotallowed.html')
    else:
        messages.error(request, "You need to log in to create a blog.")
        return redirect('user-login')
    

def delete_blog(request, blog_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog_entry = get_object_or_404(BlogEntry, id=blog_id)
            # Check if the current user is the author of the blog entry
            if blog_entry.author == request.user:
                # Delete the blog entry
                blog_entry.delete()
                return redirect('blog-home')  # Redirect to the home page after deletion
            else:
                # Return unauthorized error if the current user is not the author
                # return HttpResponse("Unauthorized", status=401)
                return render(request, 'unauthorized.html')
        else:
            # Handle the case where the request method is not POST
            return render(request, 'methodnotallowed.html')
            # return HttpResponse("Method not allowed", status=405)
    else:
        messages.error(request, "You need to log in to create a blog.")
        return redirect('user-login')
    
    
def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['fullname']
        useremail = request.POST['useremail']
        usercontact = request.POST['usercontact']
        usermessage = request.POST['usermessage']
               
        if name == "" or useremail == "" or usercontact == "" or usermessage == "":
            context['errormessage'] = "Fields Cannot be Empty"
            return render(request, 'contact.html', context)
        else:
            ci = ContactInfo.objects.create(name = name, email = useremail, contact = usercontact, message = usermessage)
            ci.save()
            return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')


def send_user_email(request):
    if request.method == 'POST':
        try:
            # Retrieve user information from the request
            fullname = request.POST.get('fullname', '')
            useremail = request.POST.get('useremail', '')
            usercontact = request.POST.get('usercontact', '')
            usermessage = request.POST.get('usermessage', '')

            if not fullname or not useremail or not usercontact or not usermessage:
                return render(request, 'contact.html', {'errormessage': 'Required fields are missing'})
                # return JsonResponse({'errormessage': 'Required fields are missing'}, status=400)

            # Construct and send the email
            send_mail(
                "Contact Query of User Submitted",
                f"Name: {fullname}\nEmail: {useremail}\nContact Number: {usercontact}\nMessage: {usermessage}",
                "amazingsiddhesh@gmail.com",
                [useremail],  # Replace with your default email address
                fail_silently=False,
            )
            return render(request, 'contact.html', {'success': 'Contact details submitted successfully !!'})
            # return JsonResponse({'success': 'Contact details submitted successfully !!'})
        except Exception as e:
            # Log the error for debugging purposes
            print(e)
            return render(request, 'contact.html', {'errormessage': 'Error submitting contact details. Please try again later !!'})
            # return JsonResponse({'error': 'Error submitting contact details. Please try again later !!'}, status=500)
    else:
        return render(request, 'contact', {'errormessage': 'Method not allowed'})
        # return JsonResponse({'error': 'Method not allowed'}, status=405)
