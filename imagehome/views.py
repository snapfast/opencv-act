from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .models import Greeting

from .forms import UploadFileForm
from .images import handle_uploaded_file


# # this function saves the file in media folder
def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name, uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'index.html')


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def image_list(request):
    return render(request, 'imagelist.html')


'''

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


'''

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file
