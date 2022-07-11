
from datetime import datetime
from tkinter import font
from unicodedata import name
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .forms import contactForm
from django.template.loader import render_to_string
from django.conf import settings
from .models import send_mail as mailmodel
import xlwt
import datetime
# Create your views here.

def ds_mail(request):
    ds = mailmodel.objects.all()
    return render(request, 'success.html',{'ds':ds})

def index(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            
            send_mail(name, content, settings.EMAIL_HOST_USER, [email], fail_silently=False )
            
            form.save()
    else: 
        form = contactForm()
    return render(request, 'index.html',{'form': form})


import pandas as pd
from django.http import JsonResponse
def export_exl(request):
   obj = mailmodel.objects.all()
   data = []
   for obj in obj:
       data.append({
           'name':obj.name,
           'email': obj.email,
           'content': obj.content
       })
   pd.DataFrame(data).to_excel('output.xlsx')
   return JsonResponse({'status': 200})



def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="send_mail.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['mane', 'email', 'content', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = mailmodel.objects.all().values_list('name', 'email', 'content')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response