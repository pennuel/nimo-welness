from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SubscriberForm

# Create your views here.
def home(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form  = SubscriberForm (request.POST)
        if form.is_valid():
            email = form.cleaned_data ['email']
            return redirect ('home')
    return render(request, 'index.html', {'form':form})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def service(request):
    return render(request, 'service-details.html')


def retreats(request):
    return render(request, 'retreats.html')


def retreat(request, retreat_name):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        author = request.POST.get('author')
        email = request.POST.get('email')
        save_info = request.POST.get('save_info')
        if request.method == 'POST':
            comment = request.POST.get('comment')
            author = request.POST.get('author')
            email = request.POST.get('email')
            save_info = request.POST.get('save_info')

    return render(request, 'retreats-details.html', {'retreat_name': retreat_name})


def rooms(request,room_name):
    return request(request, 'rooms.html', {'room_name': room_name})

def newsletter_view(request):
    form = SubscriberForm ()
    return render(request, 'newsletter.html', {'form': form})


def handle_newsletter_subscription(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return JsonResponse({'success': True})  # JSON response for success
        else:
            return JsonResponse({'success': False, 'errors': form.errors})  # JSON response with errors
    return JsonResponse({'success': False}, status=400)  # Bad request if not POST

