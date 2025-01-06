from django.shortcuts import render
from constants import services_dict
# Create your views here.
def home(request):
    return render(request, 'index.html')

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