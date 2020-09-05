from django.shortcuts import render, get_object_or_404,redirect
from .models import Menu,Oder,Review,Blog,Team
from django.views.generic import ListView,DetailView,CreateView
from .form import PlaceOrder, ReviewForm, ContantUs
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
                "reviews": Review.objects.all()
        }
        return object_list

def homeview(request):
    context={
        'menus' : Menu.objects.all(),
        'reviews' : Review.objects.all()
    }
    return render(request, 'home/index.html', context)


def place_oder(request, id=None):
    meel = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        p_form = PlaceOrder(request.POST )
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'You have successfully placed an oder wait for a call before 30 minutes')
            return redirect('home')

    else:
        
        p_form = PlaceOrder()
    context = {
        'p_form' : p_form,
        'meal' : meel
    }
    
    
    return render(request, 'home/oder_form.html', context)
    
def service(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        p_form = PlaceOrder(request.POST )
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'You have successfully placed an oder let us call you')
            return redirect('home')

    else:
        
        p_form = PlaceOrder()
    context = {
        'p_form' : p_form,
        'reviews' : reviews
    }
    return render(request, 'home/service.html', context)

def about(request):
    context = {
        'reviews' : Review.objects.all()
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
    
