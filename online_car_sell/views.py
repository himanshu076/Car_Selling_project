from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError, send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from online_car_sell.models import ContactUs, RegisterVehicle
from utils import commission, vehicle_condition, years

# admin_username- admin@gmail.com, PWD- admin

visted = False

def home(request):
    if request.method == 'GET':
        all_car = RegisterVehicle.objects.values('id', 'car_title', 'username', 
                    'mobile_no', 'images', 'images_1', 'images_2', 'images_3',
                    'images_4', 'make', 'model', 'registration_number', 'year', 
                    'condition', 'pub_date', 'vehicle_availablity', 'vehicle_price', 
                                                'platform_commission', 'net_amount',)
        paginator = Paginator(all_car, 9)
        page_number = request.GET.get("page")
        
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        global visted
        if not visted:
            messages.success(request, "<strong>Thank You! </strong> for visiting website", "visited")
            visted = True
        return render(request, 'online_car_sell/home.html', {"per_page_car": page_obj, "nbar":"home"})

def modal_data(request):
    all_car = RegisterVehicle.objects.all()
    if request.method == 'GET':
        ID = request.GET.get('id')
        all_car = all_car.get(id=ID) # So we send the company instance
        # context =
    return render(request,'online_car_sell/details.html', {'all_car':all_car})

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST["email"]
            password = request.POST["password"]
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user)
                    return redirect("home")
    return render(request, "user_auth/login.html", {})

def logout_view(request):
    logout(request)
    # logout(request, 'user_auth/logout.html', {})
    return redirect('home')

def user_register(request):
    if request.method == "GET":
        return render(request, "user_auth/register.html", {})
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if username and email and password:
                if User.objects.filter(username=username).exists():
                    # messages.HttpResponseerror(request, "Username already exists")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    # messages.ERROR(request, "Email already exists")
                    return redirect("register")
                else:
                    user = User.objects.create_user(username=username,
                                                    email=email, password=password)
                    user.save()
                    # messages.success(request, "Account created successfully")
                    return redirect("login")
            return render(request, "user_auth/register.html", {})
        else:
            # messages.ERROR(request, "Password does not matched")
            return redirect("register")

def contact(request):
    if request.method == "GET":
        return render(request, 'online_car_sell/contact.html', {})

    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        country = request.POST["country"]
        state = request.POST["state"]
        zipcode = request.POST["zipcode"]
        additional_detail = request.POST["additional_detail"]

        contact = ContactUs(first_name=firstname ,last_name=lastname, username=username,
                            email=email, mobile=mobile, address=address, country=country,
                            state=state, zip=zipcode, additional_details=additional_detail,
                            )
        contact.save()
        
        subject = f"{firstname} {lastname} wants to puchase vehicle."
        message = f'''Dear Admin,

Greetings! from Dodgy Brothers Team,

New car purchase request received from {firstname} {lastname},
And Customer wants to purchase vehicle,

Customer Message:
{additional_detail}

Please find customer detals Below and contact him ASAP,
First Name: {firstname}
Last Name: {lastname}
username: {username}
email: {email}
mobile: {mobile}
address: {address}
country: {country}
state: {state}
zipcode: {zipcode}


Thanks & Regards,
Dodgy Brothers Team
'''
        from_email = "test@gmail.com"
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email,
                            ["%s" % email], fail_silently=False,)
                # return render(request, "online_car_sell/thankyou.html")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            else:
                return render(request, "online_car_sell/thankyou.html")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")
        
@login_required(login_url='login')
def car_register(request):
    if request.method == "GET":
        is_staff = request.user.is_staff
        if is_staff:
            years_list = years
            condition_type = vehicle_condition
            return render(request, "online_car_sell/car_register.html", 
                        {'select_year':years_list, 'vehicle_condition':condition_type, "nbar":"list_your_car"})
        else:
            messages.info(request, "To register your car. Please contact to Dodgy Brothers team!")
            return redirect('home')
    if request.method == "POST":
        car_register = RegisterVehicle()
        car_register.car_title =  request.POST['car_title']
        car_register.username = request.POST['username']
        car_register.mobile_no = request.POST['mobile_no']
        car_register.image = request.POST['image']
        car_register.image_1 = request.POST['image_1']
        car_register.image_2 = request.POST['image_2']
        car_register.image_3 = request.POST['image_3']
        car_register.image_4 = request.POST['image_4']
        car_register.make = request.POST['make']
        car_register.model = request.POST['model']
        car_register.registration_no = request.POST['registration_no']
        car_register.year = request.POST['year']
        car_register.condition = request.POST['condition']
        car_register.vehicle_availablity = request.POST['vehicle_availablity']
        car_register.vehicle_price = request.POST['vehicle_price']
        _commission, _net_amount = commission(request.POST['vehicle_price'])
        car_register.platform_commission = _commission
        car_register.net_amount = _net_amount
        car_register.save()
        return render(request, 'online_car_sell/thankyou_car_register.html', {})

    # context = {'form': form}
    # return render(request, 'online_car_sell/car_register.html')

# def thank_you_car_register(request):
#     if request.method == "POST":
#         pass
#         # breakpoint()

#     return render(request, 'online_car_sell/thankyou_car_register.html', {})

# def car_delete(request):
#     pass
#     return render(request, 'online_car_sell/home', {})
