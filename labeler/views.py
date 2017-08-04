from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Image
from .forms import ImageUploadForm


def list(request):
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
        'myapp/list.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )


def index(request):
    return HttpResponse("This the home page of the Wolf Labeler App.")
