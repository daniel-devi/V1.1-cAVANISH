from django.shortcuts import render,redirect
from accounts.models import Tenant
from .models import Rooms,Payments
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
import paypalrestsdk
from django.urls import reverse
from mysite import settings

# Create your views here.
def home(request):
    
    def check_empty_fields(user):
        fields = [field.name for field in Tenant._meta.get_fields() if field.name not in ['room', "monthly_pay", 'weekly_pay']]
        empty_fields = [field for field in fields if not getattr(user, field)]
    
        if len(empty_fields) == 0 :
            #"All fields in the Tenant model are filled."
            return False 
        else:
            #"There are empty fields in the Tenant model."
            return True
        
    tenant = Tenant.objects.get(user=request.user)
    answer = check_empty_fields(tenant)

    
    context = {
        "tenant":tenant,
        "answer":answer,
    }

    return render(request, 'cavanish/home.html', context)


class SearchResultsView(ListView):
    model = Rooms
    template_name = 'cavanish/search_results.html'
    
    
def room(request, room_id):
    roomin = get_object_or_404(Rooms, pk=room_id)
    return render(request, 'cavanish/room.html')




def dashboard(request):
    tenant = Tenant.objects.get(user=request.user)
    room = tenant.room
    filtered_objects = Payments.objects.filter(room=room)
    context = {
        'tenant':tenant,
        'payments':filtered_objects,
    }
    return render(request, 'cavanish/dashboard.html' , context)
 
 

paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET,
}) 
def create_payment(request):
    tenant = Tenant.objects.get(user=request.user)
    room = tenant.room.rent_amount
    payment_amount =  room
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
        },
        "transactions": [
            {
                "amount": {
                    "total": payment_amount,  # Total amount in GBP
                    "currency": "GBP",
                },
                "description": "Payment for Product/Service",
            }
        ],
    })

    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        return render(request, 'cavanish/payment_failed.html')
    



def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        tenant = Tenant.objects.get(user=request.user)
        room = tenant.room
        room_rent= tenant.room.rent_amount
        payment_object = Payments.objects.create(payment_made_by=request.user, room=room ,amount_payed=room_rent, payment_method="Online")
        payment_object.save()
        return render(request, 'cavanish/payment_success.html')
    else:
        return render(request, 'cavanish/payment_failed.html')
    
    
    
def payment_failed(request):
    return render(request, 'cavanish/payment_failed.html')

