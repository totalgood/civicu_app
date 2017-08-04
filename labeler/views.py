from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Image
from .forms import ImageUploadForm, FileUploadForm


def list(request):
    """List of images already uploaded, and a way to upload a new one"""
    # Handle imagefile upload
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Image(file=request.FILES['imagefile'])
            newimage.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = ImageUploadForm()  # An empty, unbound form

    # Load images for the list page
    images = Image.objects.all()  # noqa

    # Render list page with the images and the form
    return render_to_response(
        'labeler/list.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )


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
    # return HttpResponse("This the index of images in the Labeler App.")


def home(request):
    images = Image.objects.all()
    return render(request, 'labeler/index.html', {'images': images})
    # return HttpResponse("This the home page of the Wolf Labeler App.")
