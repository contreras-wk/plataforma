from django.shortcuts import render

from unipol.settings.local import MEDIA_ROOT

def view_pdf(request, document):
    location = f'{MEDIA_ROOT}/documents/'
    *path, name = document.split('/')
    filePath = location + name

    return render(request, 'candidate/pdf.html', { 'doc': filePath })