from django.shortcuts import render
from myapp.models import UserInfo,CarInfo,BlogTopics,Comments
from myapp.new_car_form import UserInfoForm,CarInfoForm,BlogTopicsForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from . import forms
from django.contrib.auth.models import User


def index (request):

    form=forms.FormName()
    if request.method == 'POST':
        form=forms.FormName(request.POST)
        #if form.is_valid():

    cars_list=CarInfo.objects.order_by('date')
    usersDict={'cars_list':cars_list,'form':form}

    return render (request,'myapp/index.html',usersDict)


def dets (request):

    if request.method=='POST':
        car_id=request.POST.get('car_id')
        cars_list=CarInfo.objects.all().filter(id_no=car_id)
        return render (request,'myapp/details.html',{'cars_list':cars_list})

def delete_car (request):

    if request.method=='POST':
        car_deleted=request.POST.get('car_id')
        instance = CarInfo.objects.get(id_no=car_deleted)
        instance.delete()
        return render (request,'myapp/delete.html',{'car_deleted':car_deleted})

def edit_car (request):

    if request.method=='POST':
        id_no=request.POST.get('car_id')
        cars_list=CarInfo.objects.all().filter(id_no=id_no)
        return render (request,'myapp/edit.html',{'cars_list':cars_list})

def edit_car_2 (request):
    if request.method=='POST':
        id_no=request.POST.get('id_no')
        color=request.POST.get('color')
        engine=request.POST.get('engine')
        millage=request.POST.get('millage')
        trans=request.POST.get('trans')
        price=request.POST.get('price')

        x="failure"
        try:
            x = CarInfo.objects.get(id_no=id_no)
        except UserInfo.DoesNotExist:
            x="failure"

        x.color = color # change field
        x.engine = engine
        x.millage = millage
        x.trans = trans
        x.price = price
        x.save()

    return HttpResponseRedirect('/')


def RegistrationForm(request):
    form= UserInfoForm()
    if request.method=="POST":
        form=UserInfoForm(request.POST)

        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect('/')

        else:
            print("Error form invalid")

    return render(request,'myapp/Register.html',{'form':form})

def user_login(request):


    if request.method=='POST':
        password=request.POST.get('password')
        email=request.POST.get('email')


        try:
            created = UserInfo.objects.get(email=email, password=password)
        except UserInfo.DoesNotExist:
            created = False


        if created != False:
                request.session['email'] = email
                return HttpResponseRedirect(reverse('index'))
        else:
            superusers = User.objects.filter(is_superuser=True).values_list('email')
            bool= False

            for i in range (len(superusers)):
                if email == superusers[i][0]:
                    bool=True

            if bool==True:
                request.session['email'] = email
                request.session['super'] = 'yes'
                return HttpResponseRedirect(reverse('index'))

            else:
                return render(request,'myapp/error.html',{})

    else:
        return render(request,'myapp/login.html',{})


def logout_form (request):
    del request.session['email']
    request.session.modified = True

    if 'super' not in request.session:
        print ('nope')
    else:
        del request.session['super']
        request.session.modified = True

    return HttpResponseRedirect(reverse('index'))


def upload(request):

    carform= CarInfoForm()

    if request.method=="POST":
        carform=CarInfoForm(data=request.POST)
        if(carform.is_valid()):


            car_pic=carform.save(commit=False)

            #image uploads

            if 'car_image_1' in request.FILES:
                car_pic.car_image_1 = request.FILES['car_image_1']

            if 'car_image_2' in request.FILES:
                car_pic.car_image_2 = request.FILES['car_image_2']

            if 'car_image_3' in request.FILES:
                car_pic.car_image_3 = request.FILES['car_image_3']

            car_pic.save()
            return HttpResponseRedirect('/')

        else:
            print("Error form invalid")

    return render(request,'myapp/upload.html',{'carform':carform})

def filterSearch(request):
    if request.method=='POST':
        MAKE=request.POST.get('MAKE')
        TRANSMISSION=request.POST.get('TRANSMISSION')
        ASKING_MIN=request.POST.get('ASKING_MIN')
        ASKING_MAX=request.POST.get('ASKING_MAX')

        cars_list=CarInfo.objects.all().filter(make=MAKE,trans=TRANSMISSION,price__gte = ASKING_MIN,price__lte = ASKING_MAX)
        return render (request,'myapp/filter.html',{'cars_list':cars_list})


def blog(request):
    form= BlogTopicsForm()

    if request.method=="POST":
        form=BlogTopicsForm(request.POST)

        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect('http://127.0.0.1:8000/drafts/')

        else:
            print("Error form invalid")

    approved_posts=BlogTopics.objects.all().filter(approved='yes')
    comments=Comments.objects.all()
    front="BlogTopics object ("
    end=")"

    return render(request,'myapp/blog.html',{'form':form,'approved_posts':approved_posts,'comments':comments,'f':front,'e':end})


def drafts(request):

    my_drafts=BlogTopics.objects.all().filter(approved='no',author=request.session['email'])
    return render (request,'myapp/drafts.html',{'my_drafts':my_drafts})

def alldrafts(request):

    my_drafts=BlogTopics.objects.all().filter(approved='no')
    return render (request,'myapp/alldrafts.html',{'my_drafts':my_drafts})


def addComment(request):
    text=request.POST.get('comment')
    commenter=request.POST.get('commenter')
    post=request.POST.get('post_id')

    x="failure"
    try:
        x = BlogTopics.objects.get(id=post)
    except BlogTopics.DoesNotExist:
        x="failure"


    print (x)

    p = Comments(commenter=commenter,blog_topic_id=x,text=text )
    p.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/blog')


def delete_post (request):

    if request.method=='POST':
        draft_to_delete=request.POST.get('post_id')
        instance = BlogTopics.objects.get(id=draft_to_delete)
        instance.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/blog')

def publish_post (request):

    if request.method=='POST':
        post_to_publish=request.POST.get('post_id')
        BlogTopics.objects.filter(id=post_to_publish).update(approved='yes')
        return HttpResponseRedirect('http://127.0.0.1:8000/blog')


def delete_comment (request):

    if request.method=='POST':
        comment_to_delete=request.POST.get('comment_id')
        instance = Comments.objects.get(id=comment_to_delete)
        instance.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/blog')

def delete_entire_post (request):

    if request.method=='POST':
        post_to_delete=request.POST.get('post_id')
        instance = BlogTopics.objects.get(id=post_to_delete)
        instance.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/blog')

def edit_post (request):

    if request.method=='POST':
        post_to_edit=request.POST.get('post_id')
        post_list=BlogTopics.objects.all().filter(id=post_to_edit)
        return render (request,'myapp/edit_post.html',{'post_list':post_list})


def edit_post_2 (request):
    if request.method=='POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        text=request.POST.get('text')

        x="failure"
        try:
            x = BlogTopics.objects.get(id=id)
        except BlogTopics.DoesNotExist:
            x="failure"


        x.title = title
        x.text = text
        x.save()

    return HttpResponseRedirect('http://127.0.0.1:8000/blog')
