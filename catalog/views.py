from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/catalog.html')

def home(request):
    return render(request, 'catalog/home.html')

