from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

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