from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Sections
from .models import SubSection
from .models import FoodPlace
from .models import Order
from .models import Ordercontent
from .models import order_log
from .models import order_log_data
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token  
import os


class orderdata : 
    def __init__(self, orderlog, order_log_data_contents , total_price):
        self.orderlog = orderlog 
        self.order_log_data_contents = order_log_data_contents
        self.total_price = total_price 
        

# Create your views here.
def index(request) : 
    foodsections =  FoodPlace.objects.all()
    if request.method == "POST" : 
        place_name = request.POST['outletname']
        name = request.POST['outletownername']
        location = request.POST['outletlocation']
        desc = request.POST['outletcontent']
        messages.info(request , 'REQUEST SENT')
        return redirect('/')
        


    return render(request , 'index.html' , {'foodsections' : foodsections  })


def ordersreceived(request , pk)  :
    foodplaces = FoodPlace.objects.filter(place_name = pk)
    if foodplaces.exists():
        foodplace = foodplaces[0]
        owner_username = foodplace.owner_username
        order_logs = order_log.objects.filter()
        orderdatas = []
        if request.method == "POST" :
            a = 5 ; 
            for i in request.POST : 
                if i.isnumeric():
                    a = int(i)
                    break
            order_log_change = order_log.objects.filter(id = a)
            order_log_change_value = order_log_change[0]
            order_log_change.update(delivery_status = True)
            user = User.objects.filter(username = order_log_change_value.order_username)
            subject = 'Order Delivered'
            message = (
                f"Hi {user[0].username},\n\n"
                f"Thank you for ordering from our website.\n"
                f"Your order with order ID {order_log_change_value.id} has been delivered.\n\n"
                f"For more information, you can check the order logs on our website.\n\n"
                f"Thank you,\n"
                f"Quick Bite"
            )

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user[0].email, ]
            send_mail( subject, message, email_from, recipient_list )
        for orderlog in order_logs : 
            order_log_data_contents = order_log_data.objects.filter(order_log_id = orderlog)
            total_price = 0 
            order_log_data_contents_new = []
            for order_log_data_content in order_log_data_contents :
                if order_log_data_content.subsection_id.section_id.place_id.place_name == pk :
                    total_price += order_log_data_content.subsection_id.price * order_log_data_content.quantity
                    order_log_data_contents_new.append(order_log_data_content)
            if len(order_log_data_contents_new) > 0:
                orderdata1 = orderdata(orderlog , order_log_data_contents_new , total_price)
                orderdatas.append(orderdata1)
        return render(request , 'ordersreceived.html' , {'orderdatas'  : orderdatas , 'owner_username' : owner_username})
    else:
        return redirect('/')
def orderlog(request , pk)  :
    user = User.objects.filter(username = pk) 
    if user.exists()  :
        if request.method == 'POST'  :
            orders = Order.objects.filter(order_username = user[0].username) 
            order1 = orders[0] 
            ordercontents = Ordercontent.objects.filter(order_id = order1)
            location = request.POST['location'] 
            Phonenumber = request.POST['PhoneNumber']
            if not len(Phonenumber) == 10 or not Phonenumber.isnumeric() :
                s1 = '/confirmorder/' + user[0].username
                return redirect(s1)
            else:
                Order_log = order_log(order_username = order1.order_username , location = location , phone_number = Phonenumber)
                Order_log.save()
                recipient_list_owners= []
                for ordercontent in ordercontents : 
                    Order_log_data = order_log_data(order_log_id = Order_log , subsection_id = ordercontent.subsection_id , quantity = ordercontent.quantity)
                    Order_log_data.save()
                    owner_username = ordercontent.subsection_id.section_id.place_id.owner_username
                    user_owner = User.objects.filter(username = owner_username)
                    if user_owner[0].email not in recipient_list_owners :
                        recipient_list_owners.append(user_owner[0].email)
                    Order.objects.filter(id = order1.id).delete()
                subject = 'Order Placed'
                message = (
                    f"Hi {user[0].username},\n\n"
                    f"Thank you for ordering from our website.\n"
                    f"Your order with order ID {Order_log.id} has been placed.\n\n"
                    f"For more information, you can check the order logs on our website.\n\n"
                    f"Thank you,\n"
                    f"Quick Bite"
                )
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user[0].email, ]
                subject_owners = 'Order Recieved'
                message_owners = (
                    f"Hi,\n\n"
                    f"You have received an order from {user[0].username}.\n\n"
                    f"For more detailed information, check out the 'Orders Received' section of our website.\n\n"
                    f"Thank you,\n\n"
                    f"Quick Bite"
                )
                send_mail( subject, message, email_from, recipient_list )
                send_mail( subject_owners, message_owners, email_from, recipient_list_owners )
        orderdatas = []  
        order_logs = order_log.objects.filter(order_username = pk)
        
        for orderlog in order_logs :
            order_log_data_contents = order_log_data.objects.filter(order_log_id = orderlog)
            total_price = 0 
            
            for order_log_data_content in order_log_data_contents  :
                total_price += order_log_data_content.subsection_id.price * order_log_data_content.quantity
            orderdata1 = orderdata(orderlog , order_log_data_contents , total_price)
            orderdatas.append(orderdata1)

        return render(request , 'orderlog.html' , {'orderdatas'  : orderdatas , 'pk' : pk})
    else:
        return redirect('/')
def order(request , pk) : 
    user = User.objects.filter(username = pk) 
    if user.exists() :
        a = 5 
        order = Order.objects.filter(order_username = user[0].username) 
        if order.exists():
            order1 = order[0]
        if not order.exists() :
            order1 = Order(order_username = user[0].username)
            order1.save()
        order = Order.objects.filter(order_username = user[0].username)
        order1 = order[0]

        ordercontent2 = Ordercontent.objects.filter(order_id= order1) 
        totalprice = 0
        if request.method == 'POST' :
            if 'orderform' in request.POST:
                for i in request.POST :
                    if i.isnumeric():
                        a = int(i)
                        break
                subsection = SubSection.objects.filter(id = a)
                subsection1 = subsection[0]
                ordercontents = Ordercontent.objects.filter(order_id = order1 , subsection_id = subsection1)

            
                if ordercontents.exists() :
                    a = ordercontents[0].quantity
                    Ordercontent.objects.filter(order_id = order1 , subsection_id = subsection1).update(quantity = a)
                
                
                else:
                    ordercontent1 = Ordercontent(order_id = order1 , subsection_id = subsection1 , quantity = 1)
                    ordercontent1.save()

                ordercontent2 = Ordercontent.objects.filter(order_id= order1) 
                for ordercontent in ordercontent2 :
                    totalprice += ordercontent.subsection_id.price*ordercontent.quantity
                return render(request , 'order.html' , {'ordercontents' : ordercontent2 , 'totalprice' : totalprice , 'pk' : pk})
            if 'quantityform' in request.POST:
                for i in request.POST :
                    if i.isnumeric():
                        a = int(i)
                        break
                
                ordercontents = Ordercontent.objects.filter(id = a)
                c = ordercontents[0]
                b = ordercontents[0].quantity
                Ordercontent.objects.filter(id = a).update(quantity = b+1)
                ordercontent2 = Ordercontent.objects.filter(order_id= c.order_id) 
                for ordercontent in ordercontent2 :
                    totalprice += ordercontent.subsection_id.price*ordercontent.quantity
                return render(request , 'order.html' , {'ordercontents' : ordercontent2 , 'totalprice' : totalprice , 'pk' : pk})
            if 'quantityfrm1' in request.POST:
                for i in request.POST :
                    if i.isnumeric():
                        a = int(i)
                        break
                
                ordercontents = Ordercontent.objects.filter(id = a)
                d = ordercontents[0]
                b = ordercontents[0].quantity
                if b>1 :
                    Ordercontent.objects.filter(id = a).update(quantity = b-1)
                else:
                    Ordercontent.objects.filter(id = a).delete()
                ordercontent2 = Ordercontent.objects.filter(order_id= d.order_id) 
                for ordercontent in ordercontent2 :
                    totalprice += ordercontent.subsection_id.price*ordercontent.quantity
                return render(request , 'order.html' , {'ordercontents' : ordercontent2 , 'totalprice' : totalprice , 'pk' : pk})

            



        else :
            for ordercontent in ordercontent2 :
                totalprice += ordercontent.subsection_id.price*ordercontent.quantity
            return render(request , 'order.html' ,  {'ordercontents' : ordercontent2  ,'totalprice' : totalprice , 'pk' : pk})
    else:
        return redirect('/')
def addfoodsection(request):
    if request.method == 'POST' :
        place_name = request.POST['place']
        location = request.POST['Loc']
        owner_username  = request.POST['user1']
        name = request.POST['name']
        myfile = request.FILES['imagefile'] if 'imagefile' in request.FILES else None
        place_name = place_name.lower() 
        c = place_name[0].upper()
        s = c + place_name[1 ::] 
        
        if myfile :
            fs = FileSystemStorage()
            file = fs.save(myfile.name, myfile)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            fileurl = fs.url(file)
        
        if  User.objects.filter(username = owner_username).exists():
            if FoodPlace.objects.filter(place_name = s).exists() : 
                messages.info(request , 'FOOD OUTLET EXISTS')
                return redirect('addfoodsection')
            else:
                foodplace = FoodPlace(place_name = s ,location = location , owner_username = owner_username, name = name ,place_img = fileurl )
                foodplace.save()
                return redirect( '/')
                
        else:
            messages.info(request , 'USER DOES NOT EXIST')
            return redirect('addfoodsection')
    else:
        return render(request , 'addfoodsection.html')
    

def confirmorder(request , pk)  :
    user = User.objects.filter(username = pk)
    if user.exists() : 
        order = Order.objects.filter(order_username = user[0].username) 
        order1 = order[0]
        ordercontent2 = Ordercontent.objects.filter(order_id= order1) 
        totalprice = 0
        for ordercontent in ordercontent2 :
            totalprice += ordercontent.subsection_id.price*ordercontent.quantity
        return render(request , 'orderconfirmation.html' ,  {'ordercontents' : ordercontent2  ,'totalprice' : totalprice , 'pk' : pk})
    
    else:
        return redirect('/')

def foodplace(request , pk):
    foodsection =FoodPlace.objects.filter(place_name = pk)
    
    if foodsection.exists() :
        owner_username = foodsection[0].owner_username
        
        sections = Sections.objects.filter(place_id = foodsection[0])
        return render(request , 'foodplace.html' , {'pk1' : foodsection[0].place_name , 'sections' : sections , 'owner_username' : owner_username })
    else:
        return redirect('/')
def signup(request):
    if request.method == 'POST' :
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        password2 = request.POST['re_pass']
        
        if password == password2 :

            if User.objects.filter(email = email).exists():
                messages.info(request , 'EMAIL ALREADY EXISTS')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request , 'USERNAME ALREADY EXISTS')
                return redirect('signup')
            else:
                
                user = User.objects.create_user(username = username,email = email ,password = password)
                user.save()
                messages.info(request , 'SUCCESSFUL SIGNUP , NOW YOU CAN GO TO THE LOGIN PAGE')
                return redirect('login')
                
        else:
            
            
            messages.info(request , 'PASSWORD DO NOT MATCH')
            return redirect('signup')

            
    else:
        return render(request , 'signup.html')

    

def send_activation_email(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    message_html = render_to_string('activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    
    # Optional: Create a plaintext version of the email (alternative version)
    message_text = strip_tags(message_html)  # Strip HTML tags for plaintext version

    # Send the email with both HTML and plaintext versions
    email = EmailMultiAlternatives(mail_subject, message_text, to=[user.email])
    email.attach_alternative(message_html, "text/html")
    email.send()

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request, 'Your account has been activated successfully!')
        return redirect('login')
    else:
        messages.warning(request, 'Activation link is invalid!')
        return redirect('signup1')

    
def signup1(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        password2 = request.POST['re_pass']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL ALREADY EXISTS')
                return redirect('signup1')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME ALREADY EXISTS')
                return redirect('signup1')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False  # Deactivate account until it is confirmed
                user.save()
                
                send_activation_email(user, request)
                
                messages.info(request, 'Please confirm your email address to complete the registration')
                return redirect('login')
        else:
            messages.info(request, 'PASSWORD DO NOT MATCH')
            return redirect('signup1')
    else:
        return render(request, 'signup1.html')
def login(request):
    if request.method == 'POST' : 
        username = request.POST['your_name']
        password = request.POST['your_pass']
        user = auth.authenticate(username = username , password = password)
        
        if user is not None : 
            auth.login(request , user)
            return redirect( '/')
        else:
            messages.info(request , 'INVALID CREDENTIALS')
            return redirect('login')
    else:
        return render(request , 'login.html')
    

def logout(request) : 
    auth.logout(request)
    return redirect('/')

def addsection(request , pk)  :
    foodsection =FoodPlace.objects.filter(place_name = pk)

    if foodsection.exists():
        foodplace = foodsection[0]
        owner_username = foodplace.owner_username
        if request.method == 'POST' :
            section_name = request.POST['name']
            desc = request.POST['desc']
            price_lower  = request.POST['l_price']
            price_higher = request.POST['h_price']
            category = request.POST['Category']
            myfile = request.FILES['imagefile'] if 'imagefile' in request.FILES else None
            section_name = section_name.lower() 
            c = section_name[0].upper()
            s = c + section_name[1 ::] 
            s1 = '/addsection/' + pk
            s2 = '/foodplace/' + pk
            if myfile :
                fs = FileSystemStorage()
                file = fs.save(myfile.name, myfile)
                # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
                fileurl = fs.url(file)

            if price_lower.isnumeric() and price_higher.isnumeric() :
                if Sections.objects.filter(section_name = s , place_id = foodsection[0]).exists() : 
                    messages.info(request , 'SECTION NAME EXISTS')
                    return redirect(s1)
                if category not in ['S' , 'B' , 'M'] :
                    messages.info(request , 'INVALID CATEGORY')
                    return redirect(s1)
                else:
                    section = Sections(place_id = foodsection[0] , section_name = s , price_lower = int(price_lower) , price_higher = int(price_higher) , img = fileurl , desc = desc , section_category = category )
                    section.save()
                    return redirect( s2)

            else:
                messages.info(request , 'ENTER VALID PRICES')
                return redirect(s1)

            
        else:
            return render(request , 'addsection.html' , {'owner_username'  : owner_username})
    else:
        return redirect('/')
    
def subsection(request , pk1 , pk2) :
    foodsection = FoodPlace.objects.filter(place_name = pk1)
    if foodsection.exists():
        section = Sections.objects.filter(section_name = pk2 , place_id = foodsection[0])
    else:
        return redirect( '/')
    
    if  section.exists() :
        owner_username = foodsection[0].owner_username
        subsections = SubSection.objects.filter(section_id = section[0])
        return render(request , 'subsection.html' , {'pk1' : section[0].place_id.place_name ,  'pk2' : section[0].section_name , 'subsections' : subsections , 'owner_username' : owner_username})
    else:
        return redirect( '/')
    
def addsubsection(request , pk1 , pk2) :
    foodsection = FoodPlace.objects.filter(place_name = pk1)
    if foodsection.exists():
        foodplace = foodsection[0]
        section = Sections.objects.filter(section_name = pk2 , place_id = foodsection[0])
    else:
        return redirect( '/')
    
    if section.exists() :
        owner_username = foodplace.owner_username
        if request.method == 'POST' :
            subsection_name = request.POST['name']
            price  = request.POST['price']
            myfile = request.FILES['imagefile'] if 'imagefile' in request.FILES else None
            subsection_name = subsection_name.lower() 
            c = subsection_name[0].upper()
            s = c + subsection_name[1 ::] 
            s1 = '/addsubsection/' + section[0].place_id.place_name + '/' + section[0].section_name
            s2 = '/subsection/' + section[0].place_id.place_name + '/' + section[0].section_name
            if myfile :
                fs = FileSystemStorage()
                file = fs.save(myfile.name, myfile)
                # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
                fileurl = fs.url(file)
        
            if price.isnumeric()  :
                if SubSection.objects.filter(subsection_name = s , section_id = section[0]).exists() : 
                    messages.info(request , 'SUBSECTION NAME EXISTS')
                    return redirect(s1)
                else:
                    subsection = SubSection( section_id = section[0] , subsection_name = s, price = int(price) ,  sub_img = fileurl )
                    subsection.save()
                    return redirect(s2)
                
            else:
                messages.info(request , 'ENTER VALID PRICE')
                return  redirect(s1 )

            
        else:
            return render(request , 'addsubsection.html' , {'owner_username' : owner_username})
    else:
        return redirect( '/')
    
