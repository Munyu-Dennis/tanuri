from django.shortcuts import render, get_object_or_404,redirect
from .models import Menu,Oder,Reviews,Blog,Team,OrderIn
from django.views.generic import ListView,DetailView,CreateView
from .form import PlaceOrder, ReviewForm, ContantUs, OrderIn1,PlaceOrderI
from django.contrib import messages

class MenuListView(ListView):
    #model = Menu
    template_name = 'home/index.html'#<app>/<model>_<view_type>.html
    context_object_name = 'menus'
    ordering = ['price']
    def get_queryset(self, **kwargs):
        object_list = super(MenuListView, self).get_context_data(**kwargs)
        object_list = {
                "menus": Menu.objects.all(),
                "reviews": Reviews.objects.all()
        }
        return object_list

def homeview(request):
    context={
        'menus' : Menu.objects.all(),
        'reviews' : Reviews.objects.all()
    }
    return render(request, 'home/index.html', context)


def place_oder(request, id=None):
    meel = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        p_form = PlaceOrder(request.POST )
        t_form = PlaceOrder(request.POST )
        if  p_form.is_valid() :
            p_form.save()

            messages.success(request, f'You have successfully placed an oder, order on the way')
            return redirect('home')
        elif t_form.is_valid():
            t_form.save()
            messages.success(request, f'You have successfully placed an oder wait for a call before 30 minutes')
            return redirect('place-oder')

    else:

        p_form = PlaceOrder()
    context = {
        'p_form' : p_form,
        'meal' : meel
    }


    return render(request, 'home/oder_form.html', context)
'''
def service(request):
    # query = get_object_or_404.GET()
    person = False
    persons = 0
    if request.method == 'GET':

        query = request.GET.get('persons')
        if query is not None:
           persons = int(query)
           messages.success(request, f'Please scroll down to place the orders for the {persons} persons')
           person = True
    else:
        person = False

    if request.method == 'POST':
        p_form = PlaceOrder(request.POST )
        if  p_form.is_valid():
            p_form.save()
            if persons > 1:
                messages.success(request, f'You have successfully placed Orders for the {persons}, Orders on the way')
            else:
                messages.success(request, f'You have successfully placed an oder, order on the way')


            return redirect('home')

    else:

        p_form = PlaceOrder()
    context = {
        'p_form' : p_form,
        'reviews' : Reviews.objects.all(),
        'person' : person,
        'persons': range(persons),
        'p' : persons,
        'menus' : Menu.objects.all()
    }
    return render(request, 'home/service.html', context)

'''
def service(request):
    # query = get_object_or_404.GET()
    person = False
    persons = 0
    one,two,three,four,five,six=False,False,False,False,False,False
    if request.method == 'GET':

        query = request.GET.get('persons')
        if query is not None:
           persons = int(query)
           messages.success(request, f'Please scroll down to place the orders for the {persons} persons')
           person = True
           if persons == 2:
               two=True
           elif persons == 3:
                three = True
           elif persons == 4:
                four = True
           elif persons == 5:
                five = True
           elif persons == 6:
                six = True

    else:
        person = False
        one = True

    if request.method == 'POST':
        s_form = PlaceOrderI(request.POST)
        if  s_form.is_valid():
            s_form.save()
            #send_mail()
            messages.success(request, f'You have successfully placed an oder, order on the way')
            return redirect('home')

    else:
        s_form = PlaceOrderI()


    context = {
        's_form' : s_form,
        #'p_form' : p_form,
        'reviews' : Reviews.objects.all(),
        'person' : person,
        'persons': range(persons),
        'p' : persons,
        'menus' : Menu.objects.all(),
        'one':one,
        'two':two,
        'three':three,
        'four':four,
        'five':five,
        'six':six
    }
    return render(request, 'home/service.html', context)
def about(request):
    context = {
        'reviews' : Reviews.objects.all()
    }
    return render(request, 'home/aboutus.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'home/blog.html'#<app>/<model>_<view_type>.html
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 5



def contant(request):
    if request.method == 'POST':
        c_form = ContantUs(request.POST )
        if  c_form.is_valid():
            c_form.save()
            messages.success(request, f'Thanks for your feedback we will get  back to you before 2 days, keep this information between us')
            return redirect('home')

    else:

        c_form = ContantUs()
    context = {
        'c_form' : c_form
    }
    return render(request, 'home/contant.html', context)

def reviewform(request):
    if request.method == 'POST':
        r_form = ReviewForm(request.POST )
        if  r_form.is_valid():
            r_form.save()
            messages.success(request, f'Thanks for your review please scroll below to check it out and others to')
            return redirect('home')

    else:

        r_form = ReviewForm()
    context = {
        'r_form' : r_form
    }
    return render(request, 'home/reviewform.html', context)

