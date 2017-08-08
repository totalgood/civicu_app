from django.shortcuts import render, redirect
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from .models import Image
from .forms import FileUploadForm


def form_file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
    return render(request, 'labeler/form_file_upload.html', {
        'form': form
    })


def index(request):
    images = Image.objects.all()
    return render(request, 'labeler/index.html', {'images': images})
