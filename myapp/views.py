# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myapp.models import Document
from myapp.forms import DocumentForm, MailForm
from myapp.main import run
from myapp.emailsender import send


def list(request):
    # Handle file upload
    if request.method == 'POST':
        if request.POST.get("form1")!="":
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                newdoc.save()

                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('list'))

        elif request.POST.get("form2")!="":
             mail = request.POST.get("mail")
             dropdown = request.POST.get("ident")
             #plik = {{ document.docfile.url }}
             # run(lokalizacja pliku, lokalizacja modelu, nazwa modelu)
             #send (mail,link)
             #return HttpResponseRedirect("/myapp/"+dropdown)

    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )


def detail(request, document_id):
    documents = Document.objects.all()
    try:
        documents = Document.objects.get(pk=document_id)
    except Document.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'detail.html', {'documents': documents})

def model(request, document_id):
    documents = Document.objects.all()
    try:
        documents = Document.objects.get(pk=document_id)
    except:
        raise Http404("Document does not exist")
    return render(request, 'model.html', {'documents': documents})