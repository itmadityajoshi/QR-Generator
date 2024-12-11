from django.shortcuts import render
from .forms import QrCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QrCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # print(res_name, url)

            #Generate QR Code
            qr =  qrcode.make(url)
            # print(qr)
            file_name = res_name.replace(" ", "_").lower()+ '_menu.png'
            filepath = os.path.join(settings.MEDIA_ROOT, file_name) #image path
            qr.save(filepath)

            # create Image URL
            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'res_name' : res_name,
                'qrlimage' : qr_url
            }
            return render (request, 'qr_result.html', context)

    else:
        form = QrCodeForm
        context = {
            'form': form,
        }
        return render (request, 'generate_qr.html', context)
