from django.shortcuts import render
from constants import services_dict
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


# Add the template from prompt engineering for the services.
    # 'mindfulness': {
    #     'title': 'Mindfulness',
    #     'header text': 'Mindfulness',
    #     'title_details': 'describes what we are doing in the service',
    #     'description': 'give an indepth description of the service and how we do it and what i will do from the person',
    #     'benefits': [
    #         "benefits in a list format"
    #     ],
    #     'assurances': 'assurances of the service and what it can do for the customer',
    # },


def service_details(request, services_selected):

    service_details = services_dict.get(services_selected)
    services_title = [title for title, _ in services_dict.items()]
    print(services_title)
    if service_details:
        return render(request, 'service-details.html', {'service': service_details,'titles' : services_title})
    else:
        return render(request, '404.html', status=404)


def service(request):
    services = [(title,service) for title, service in services_dict.items()]
    print(services)
    return render(request, 'services.html', {'services': services})

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

