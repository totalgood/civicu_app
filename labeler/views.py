from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from labeler_site.labeler.models import Image
from labeler_site.labeler.forms import ImageForm


def list(request):
    # Handle imagefile upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Image(file=request.FILES['imagefile'])
            newimage.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = ImageForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
def index(request):
    return HttpResponse("This the home page of the Wolf Labeler App.")
