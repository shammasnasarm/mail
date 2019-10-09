from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from user.models import *
from data.models import *
import datetime
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from data.models import *
##from django.views.decorators.cache import cache_control


# Create your views here.


def register(request):
    ob=Country.objects.all()
    oc=hobby.objects.all()
    return render(request,"user/registration.html",{"data":ob,"hob":oc,"sec":od})

def saveuser(request):
    if request.method=="POST":
        first_name = request.POST['txtfirst']
        last_name = request.POST['txtlast']
        email = request.POST['txtemail']
        username = request.POST['txtuser']
        password = request.POST['txtpass']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        user.save()
        return HttpResponseRedirect("home.html",{"sucs":"Register sucessfully completed"})
    else:
        return render(request,"home.html",{"sucs":"Register sucessfully completed"})

def saveuserdetails(request):
    if request.method=='POST':
        dob =request.POST['txtage']
        gender =request.POST['radgender']
        country =request.POST['country']
        state =request.POST['state']
        district =request.POST['district']
        phone =request.POST['txtphone']

        user_details.objects.create(User_id=request.user,DOB=dob,Gender=gender,Country=country,State=state,District=district,Phone_No=phone)


        return redirect(inbox)

def getstate(request):
    countryid=request.GET.get('cid')
    statemodel=State.objects.filter(Country=countryid)
    return render(request,'user/state_dropdown_list_option.html',{"state":statemodel})

def getdistrict(request):
    stateid=request.GET.get('sid')
    districtmodel=District.objects.filter(State=stateid)
    return render(request,'user/district_dropdown_list_option.html',{"district":districtmodel})


def validate_username(request):
    username = request.GET.get('Username', None)
    print(username)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

##@cache_control(no_cache=True, must_revalidate=True, no_store=True)
##@login_required(login_url='login')
def userlogin(request):
    if request.method=="POST":
        usr=request.POST['txtuser']
        pas=request.POST['txtpas']
        user = authenticate(username=usr,password=pas)

        if user is not None:
            login(request,user)
            ob = user_details.objects.filter(User_id=request.user)
            if ob.count():
                return redirect('inbox')
            else:
                return redirect(profile)
        else:
            return render(request,"home.html",{"msg":"Invalid Username or Password"})
    else:
        return render(request,"home.html",{"msg":"Invalid Username or Password"})


#        ob=user_login.objects.filter(Username=usr)
#        if ob.count()==1:
#            en_pas = ob[0].Password
#            verification = pbkdf2_sha256.verify(pas,en_pas)
#            print("a")



##        ob=user_login.objects.filter(Username=usr,Password=pas)
##        if ob.count()==1:
#            if verification == 1:
#                request.session["id"]=ob[0].id
                #return render(request,"user/home.html")
#                return redirect('inbox')
#            else:
#                return render(request,"home.html",{"msg":"Invalid Username or Password"})

#        else:
#                return render(request,"home.html",{"msg":"Invalid Username or Password"})



def forgot(request):
    ob=User.objects.all()
    return render(request,"user/forgotpassword.html",{"data":ob})

def changeforgotpas(request):
    if request.method=="POST":
        usr=request.POST['txtuser']
        qus=request.POST['ddlques']
        ans=request.POST['txtans']
        ob=User.objects.filter(username=usr,Security_Ques=qus,Answer=ans)
        if ob.count()>0:
            return render(request,"user/newpassword.html",{"data":usr})
        else:
            oc=User.objects.all()
            return render(request,"user/forgotpassword.html",{"data":oc,"msg":"The answer you are ender is wrong"})


def setnewpass(request):
    if request.method=="POST":
        usr=request.POST['txtuser']
        new=request.POST['txtnewpas']
        con=request.POST['txtconpas']
        if new==con:
            en_password=pbkdf2_sha256.encrypt(new,rounds=12000,salt_size=32)
            ob=user_login.objects.filter(Username=usr).update(Password=en_password)
            return render(request,"home.html",{"pas":"Password changed"})
        else:
            return render(request,"user/newpassword.html",{"data":usr,"msg":"Password is not matching"})

def composemail(request):
    return render(request,"user/composemail.html")

def sendmail(request):
    if request.method=="POST":
        fr=request.user
        frid=fr.id
        to=request.POST['txtto']
        sub=request.POST['txtsub']
        cnt=request.POST['txtcnt']
        date=datetime.date.today()
        if len(request.FILES)!=0:
            t_file=request.FILES["upload"]
        else:
            t_file='nopic'
        
        ob=User.objects.get(username=to)
        if ob:
            oc=User.objects.get(username=to)
            od=oc.id
            oc=user_mailcompose_tb(From=request.user,To=od,Subject=sub,Content=cnt,Date=date,File=t_file,Status='Pending')
            oc.save()
            return HttpResponseRedirect("user/composemail.html",{"Msg":"Mail send successfully"})
##            return render(request,"user/composemail.html")
        else:
            return render(request,"user/composemail.html",{"msg":"There is no such user"})
    else:
        return render(request,"user/composemail.html")

def inbox_test(request):
    if request.user.is_authenticated:
        print(request.user)
        ob=user_mailcompose_tb.objects.filter(To=request.user.id,Status="filtered")
        oc=ob[::-1]
        return render(request,"user/inbox.html",{'data':oc})
        

def inbox(request):
    ob=user_details.objects.filter(User_id=request.user)

#    usr=ob[0].username
#    yer=user_register.objects.filter(Username=usr)
    if ob.count():
        y=ob[0].DOB
        ls=y.split('-')
        x=int(ls[0])
        cdate=int(datetime.date.today().strftime("%Y"))
    
#    userregisterinstance=user_register.objects.filter(Username=yer[0].Username)
        ageofuser=cdate-x
        agefactor=age_factor.objects.filter(Min_age__lte=ageofuser,Max_age__gte=ageofuser).values_list('Age_factor')

        for agefactor in agefactor:
            user_mailcompose_tb.objects.filter(To=request.user.id,Content__icontains=agefactor[0]).update(Status='filtered')


        husr=user_hobby.objects.filter(Username=request.user.username).values_list('Hobby')
        for hobby in husr:

            hob=hobby.objects.filter(Hobby=hobby[0])
            idofhobby=int(hob[0].id)
            hobbyfactor=hobby_factor.objects.filter(Hobby_id=idofhobby).values_list('Hobby_factor')
            for hobfact in hobbyfactor:
                user_mailcompose_tb.objects.filter(To=request.user.id,Content__icontains=hobfact[0]).update(Status='filtered')

##  filter contact:    
        fltcont=contacts_tb.objects.filter(User_id=request.user.id)
        if fltcont.count()>=1:
        
            for con in fltcont:

                frm=con.Contact_id
                user_mailcompose_tb.objects.filter(To=request.user.id,From=frm).update(Status='filtered')

        od = user_mailcompose_tb.objects.filter(To=request.user.id, Status="filtered")
        oc = od[::-1]
        return render(request,"user/inbox.html",{"data":oc})
    else:
        return redirect(profile)

def viewmessage(request,msg_id):
    ob=user_mailcompose_tb.objects.filter(id=msg_id)
    return render(request,"user/message.html",{"data":ob})

def savemail(request):
    if request.method=="POST":
        msg=request.POST.getlist('chk[]')
        for m in msg:
            mails=user_mailcompose_tb.objects.filter(id=m)
            ob=user_mailsave_tb(User_id=request.user.id,Mail_id_id=mails[0].id)
            ob.save()
            oc=user_mailcompose_tb.objects.filter(To=request.user.id)
        return HttpResponseRedirect("user/inbox.html",{"data":oc})
    else:
        oc=user_mailcompose_tb.objects.filter(To=request.user.id)
        return render(request,"user/inbox.html",{"data":oc})

def savedmails(request):
    if request.user != None:
        ob=user_mailsave_tb.objects.filter(User_id=request.user.id)
        return render(request,"user/savedmails.html",{"data":ob})
    else:
        return render(request,"home.html")

def spam(request):
    ob=user_mailcompose_tb.objects.filter(To=request.user.id,Status="Pending")
    return render(request,"user/spam.html",{"data":ob})

def addcontact(request):
    return render(request,"user/addcontact.html")


def savecontact(request):
    if request.method=="POST":
        usr=request.POST['txtusr']
        ch=User.objects.filter(username=usr)
        if ch.count()==1:
            cntid=ch[0].id
            name=ch[0].first_name
            ob=contacts_tb(User_id=request.user.id,Contact_id=cntid,Date=datetime.date.today(),Name=name)
            oc=contacts_tb.objects.filter(User_id=request.user.id,Contact_id=cntid)
            if oc.count()==1:
                return render(request,"user/addcontact.html")
            else:
                ob.save()
                return render(request,"user/home.html")
        else:
            return render(request,"user/addcontact.html")


def profile(request):
    ob=user_details.objects.filter(User_id=request.user)
    oc=Country.objects.all()
    oe=hobby.objects.all()
    
    return render(request,"user/home.html",{"data":ob,"cnt":oc,"hob":oe})

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request(request):
    logout(request)
    return render(request,"home.html")

def enlargefile(request,msg_id):
    ob=user_mailcompose_tb.objects.filter(id=msg_id)
    return render(request,"user/file.html",{"data":ob})

def forward(request,msg_id):
    if request.method=="POST":
        ob=user_mailcompose_tb.objects.filter(id=msg_id)
        fr=request.user
        date=datetime.date.today()
        to=request.POST['txtto']
        od=User.objects.get(username=to)
        if od:
            oc=User.objects.get(username=to)
            od=oc.id
            oc=user_mailcompose_tb(From=fr,To=od,Subject=ob[0].Subject,Content=ob[0].Content,Date=date,File=ob[0].File,Status='Pending')
            oc.save()
            return redirect('nex')
        else:
            return render(request,"user/composemail.html")


def nex(request):
    return render(request,"user/composemail.html")

