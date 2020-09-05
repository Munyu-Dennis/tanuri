from django.shortcuts import render,get_object_or_404
from home.models import Blog
from django.views.generic import ListView
from .models import Comments
from .form import CommentForm
class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'#<app>/<model>_<view_type>.html
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 5

def blogdetail(request, id=None):
    blog = get_object_or_404(Blog, id=id)
    comments = Comments.objects.filter(Title=blog.title)
    if request.method == 'POST':
        c_form = PlaceOrder(request.POST )
        if  c_form.is_valid():
            c_form.save()
            messages.success(request, f'')
            return redirect('blog')

    else:
        
        c_form = PlaceOrder()
    context = {
        'blog':blog
    }
    return render(request, 'blog.blogdetail.html', context)
