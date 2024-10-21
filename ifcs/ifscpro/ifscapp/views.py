from django.shortcuts import render
from django.http import HttpResponse
import requests

def ifsc_lookup(request):
    ifsc_code = ''
    branch_details = {}
    error_message = None

    if request.method == 'POST':
        ifsc_code = request.POST.get('ifsc_code').strip()
        
        # Check if IFSC code is provided
        if ifsc_code:
            try:
                # Make a request to Razorpay IFSC API
                response = requests.get(f'https://ifsc.razorpay.com/{ifsc_code}')
                
                # Check if the response is OK
                if response.status_code == 200:
                    branch_details = response.json()
                else:
                    error_message = 'Invalid IFSC code. Please try again.'
            except requests.RequestException as e:
                error_message = 'Error fetching data from the API. Please try again later.'

    # context = {
    #     'ifsc_code': ifsc_code,
    #     'branch_details': branch_details,
    #     'error_message': error_message,
    # }
    
    return render(request, 'front.html',  branch_details)

