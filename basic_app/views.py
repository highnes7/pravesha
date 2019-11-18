from django.conf import settings
from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Log
from django.core.mail import send_mail
from django.template.loader import render_to_string

#pdf________________________
from django.views.generic import View
from django.utils import timezone
from .render import Render


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileInfoForm(data=request.POST)
    return render(request,'basic_app/index.html',{'user_form':user_form,
                           'profile_form':profile_form,})

def coordinator(request):
    footfall = len(UserProfileInfo.objects.filter(cs=False))-2
    pp_l = len(UserProfileInfo.objects.filter(pp=True))
    bat_l = len(UserProfileInfo.objects.filter(bat=True))
    tq_l = len(UserProfileInfo.objects.filter(tq=True))
    ar_l = len(UserProfileInfo.objects.filter(ar=True))
    aio_l = len(UserProfileInfo.objects.filter(aio=True))
    ty_l = len(UserProfileInfo.objects.filter(ty=True))
    syt_l = len(UserProfileInfo.objects.filter(syt=True))
    mod_l = len(UserProfileInfo.objects.filter(mod=True))
    th_l = len(UserProfileInfo.objects.filter(th=True))
    pubg_l = len(UserProfileInfo.objects.filter(pubg=True))
    logleft = len(User.objects.filter(last_login=None))
    left = len(UserProfileInfo.objects.filter(cs=False,pp=False,bat=False,tq=False,ar=False,aio=False,ty=False,syt=False,mod=False,th=False,pubg=False)) - 2
    return render(request, 'basic_app/coordinator.html',{'footfall':footfall ,'pp_l':pp_l,'bat_l':bat_l,'tq_l':tq_l,'ar_l':ar_l,'aio_l':aio_l,'ty_l':ty_l,'syt_l':syt_l,'mod_l':mod_l,'th_l':th_l,'pubg_l':pubg_l,'left':left,'logleft':logleft})

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST )
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)

            if User.objects.filter(email=user.email).exists() or UserProfileInfo.objects.filter(mob_no=profile.mob_no) or UserProfileInfo.objects.filter(college_reg_id=profile.college_reg_id):
                print("Exixt")
            else:
                # Save User Form to Database
                user = user_form.save()

                # Hash the password
                user.set_password(user.password)
                codeg=1110+user.id
                user.username='P19'+str(codeg)

                # Update with Hashed password
                user.save()

                # Now we deal with the extra info!

                # Can't commit yet because we still need to manipulate


                # Set One to One relationship between
                # UserForm and UserProfileInfoForm
                profile.user = user

                log = Log()
                log.mob_no_log = profile.mob_no
                log.email_log = user.email
                log.refuser = user.username
                log.save()

                # Check if they provided a profile picture
                #if 'profile_pic' in request.FILES:
                #print('found it')
                # If yes, then grab it from the POST form reply
                #profile.profile_pic = request.FILES['profile_pic']

                # Now save model
                profile.save()

                # Registration Successful!
                registered = True
                subject = "Registration Sucessful Pravesha'19"
                message = render_to_string("basic_app/message_body.html",{'regid':user.username ,'fname':user.first_name,'lname':user.last_name})
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject,message,from_email,to_list,fail_silently=True)



        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    if registered== True:

        return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'username':user.username})
    else:
        return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           })

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username').upper()
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                if user.profile.cs == False:
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponseRedirect('coordinator')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return HttpResponseRedirect(reverse('index'))


def food_pref_updt(request):
        if request.method == 'POST':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(food_pref=request.POST.get('fp'))
            return HttpResponseRedirect(reverse('index'))

def participate(request):
    if request.method == 'POST':
        if request.POST.get('event') == 'pp':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(pp=True)
        elif request.POST.get('event') == 'bat':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(bat=True)
        elif request.POST.get('event') == 'tq':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(tq=True)
        elif request.POST.get('event') == 'ar':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(ar=True)
        elif request.POST.get('event') == 'aio':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(aio=True)
        elif request.POST.get('event') == 'ty':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(ty=True)
        elif request.POST.get('event') == 'syt':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(syt=True)
        elif request.POST.get('event') == 'mod':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(mod=True)
        elif request.POST.get('event') == 'th':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(th=True)
        elif request.POST.get('event') == 'pubg':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(pubg=True)
        # elif request.POST.get('event') == 'tiktok':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(tiktok=True)
        # elif request.POST.get('event') == 'opm':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(opm=True)
        # elif request.POST.get('event') == 'mc':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(mc=True)
        # elif request.POST.get('event') == 'meme':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(meme=True)
        return HttpResponseRedirect(reverse('index'))

def departicipate(request):
    if request.method == 'POST':
        if request.POST.get('event') == 'pp':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(pp=False)
        elif request.POST.get('event') == 'bat':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(bat=False)
        elif request.POST.get('event') == 'tq':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(tq=False)
        elif request.POST.get('event') == 'ar':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(ar=False)
        elif request.POST.get('event') == 'aio':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(aio=False)
        elif request.POST.get('event') == 'ty':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(ty=False)
        elif request.POST.get('event') == 'syt':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(syt=False)
        elif request.POST.get('event') == 'mod':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(mod=False)
        elif request.POST.get('event') == 'th':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(th=False)
        elif request.POST.get('event') == 'pubg':
            UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(pubg=False)
        # elif request.POST.get('event') == 'tiktok':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(tiktok=False)
        # elif request.POST.get('event') == 'opm':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(opm=False)
        # elif request.POST.get('event') == 'mc':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(mc=False)
        # elif request.POST.get('event') == 'meme':
        #     UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(meme=False)
        return HttpResponseRedirect(reverse('index'))

def user(request):
    return render(request, 'basic_app/user.html')

@login_required
def adminpanel(request):
    return render(request, 'basic_app/adminpanel.html')


@login_required
def cs_pp(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_pp="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_pp'))
    return render(request,'basic_app/cs_pp.html',{'participants_list':participants_list})

@login_required
def cs_bat(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_bat="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_bat'))
    return render(request,'basic_app/cs_bat.html',{'participants_list':participants_list})

@login_required
def cs_tq(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_tq="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_tq'))
    return render(request,'basic_app/cs_tq.html',{'participants_list':participants_list})

@login_required
def cs_ar(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_ar="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_ar'))
    return render(request,'basic_app/cs_ar.html',{'participants_list':participants_list})

@login_required
def cs_aio(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_aio="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_aio'))
    return render(request,'basic_app/cs_aio.html',{'participants_list':participants_list})

@login_required
def cs_ty(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_ty="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_ty'))
    return render(request,'basic_app/cs_ty.html',{'participants_list':participants_list})

@login_required
def cs_syt(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_syt="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_syt'))
    return render(request,'basic_app/cs_syt.html',{'participants_list':participants_list})

@login_required
def cs_mod(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_mod="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_mod'))
    return render(request,'basic_app/cs_mod.html',{'participants_list':participants_list})

@login_required
def cs_th(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_th="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_th'))
    return render(request,'basic_app/cs_th.html',{'participants_list':participants_list})

@login_required
def cs_pubg(request):
    participants_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        participant = User.objects.get(username=request.POST.get('regid'))
        participant.profile.status_pubg="P"
        participant.profile.save()
        return HttpResponseRedirect(reverse('basic_app:cs_pubg'))
    return render(request,'basic_app/cs_pubg.html',{'participants_list':participants_list})







@login_required
def pp_winners(request):
    if len(UserProfileInfo.objects.filter(status_pp= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_pp= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_pp="W"
            runnerup.profile.status_pp="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:pp_winners'))
        return render(request,'basic_app/pp_winners.html')
    else:
        return HttpResponse("Event Closed")



@login_required
def bat_winners(request):
    if len(UserProfileInfo.objects.filter(status_bat= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_bat= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_bat="W"
            runnerup.profile.status_bat="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:bat_winners'))
        return render(request,'basic_app/bat_winners.html')
    else:
        return HttpResponse("Event Closed")

@login_required
def tq_winners(request):
    if len(UserProfileInfo.objects.filter(status_tq= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_tq= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_tq="W"
            runnerup.profile.status_tq="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:tq_winners'))
        return render(request,'basic_app/tq_winners.html')
    else:
        return HttpResponse("Event Closed")


@login_required
def ar_winners(request):
    if len(UserProfileInfo.objects.filter(status_ar= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_ar= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_ar="W"
            runnerup.profile.status_ar="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:ar_winners'))
        return render(request,'basic_app/ar_winners.html')
    else:
        return HttpResponse("Event Closed")

@login_required
def aio_winners(request):
    if len(UserProfileInfo.objects.filter(status_aio= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_aio= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_aio="W"
            runnerup.profile.status_aio="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:aio_winners'))
        return render(request,'basic_app/aio_winners.html')
    else:
        return HttpResponse("Event Closed")

@login_required
def ty_winners(request):
    if len(UserProfileInfo.objects.filter(status_ty= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_ty= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_ty="W"
            runnerup.profile.status_ty="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:ty_winners'))
        return render(request,'basic_app/ty_winners.html')
    else:
        return HttpResponse("Event Closed")


@login_required
def syt_winners(request):
    if len(UserProfileInfo.objects.filter(status_syt= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_syt= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_syt="W"
            runnerup.profile.status_syt="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:syt_winners'))
        return render(request,'basic_app/syt_winners.html')
    else:
        return HttpResponse("Event Closed")

@login_required
def mod_winners(request):
    if len(UserProfileInfo.objects.filter(status_mod= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_mod= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_mod="W"
            runnerup.profile.status_mod="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:mod_winners'))
        return render(request,'basic_app/mod_winners.html')
    else:
        return HttpResponse("Event Closed")

@login_required
def th_winners(request):
    if len(UserProfileInfo.objects.filter(status_th= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_th= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_th="W"
            runnerup.profile.status_th="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:th_winners'))
        return render(request,'basic_app/th_winners.html')
    else:
        return HttpResponse("Event Closed")

@login_required
def pubg_winners(request):
    if len(UserProfileInfo.objects.filter(status_pubg= 'W')) == 0 and len(UserProfileInfo.objects.filter(status_pubg= 'RU')) == 0 :
        if request.method == 'POST':
            winner = User.objects.get(username=request.POST.get('wregid'))
            runnerup = User.objects.get(username=request.POST.get('ruregid'))
            winner.profile.status_pubg="W"
            runnerup.profile.status_pubg="RU"
            winner.profile.save()
            runnerup.profile.save()
            return HttpResponseRedirect(reverse('basic_app:pubg_winners'))
        return render(request,'basic_app/pubg_winners.html')
    else:
        return HttpResponse("Event Closed")





@login_required
def registrationdesk(request):
    # reguser_list = User.objects.filter(is_staff=False)
    if request.method == 'POST':
        searchlist = User.objects.filter(username=request.POST.get('regid'))
        return render(request,'basic_app/registrationsearch.html',{'searchlist':searchlist})

    return render(request,'basic_app/registrationdesk.html')

@login_required
def paymentupdate(request):
    if request.method == 'POST':
        UserProfileInfo.objects.filter(mob_no=request.POST.get('no')).update(payment_stats=True,food_pref=request.POST.get('fp'))
        return render(request,'basic_app/registrationdesk.html')


def Pdf(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,

    }
    return Render.render('basic_app/pdf.html', params)



def pp_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,

    }
    return Render.render('basic_app/ppreport.html', params)

def bat_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,

    }
    return Render.render('basic_app/bat_report.html', params)

def tq_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/tq_report.html', params)


def adzpreloaded_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/adzapreloaded_report.html', params)



def aio_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/assembleio_report.html', params)

def typist_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/typist_report.html', params)

def showyourtalent_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/showyourtalent_report.html', params)

def mod_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/momentoftheday_report.html', params)

def treasurehunt_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/trasurehunt_report.html', params)

def pubg_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/pubg_report.html', params)

def certificate_report(View):

    user_list = User.objects.filter(is_staff=False)
    today = timezone.now()
    params = {
        'today': today,
        'user_list': user_list,
    }
    return Render.render('basic_app/certificate_report.html', params)
