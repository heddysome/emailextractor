from django.shortcuts import render, render_to_response
from django.template.response import TemplateResponse


# Create your views here.
def page_emails(request):
    return TemplateResponse(request, 'PageEmails.html')
