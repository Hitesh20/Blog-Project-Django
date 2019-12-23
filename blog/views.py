from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView,DeleteView,UpdateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin    ## this will restrict user to add new post if he is not logged in
from django.contrib.auth.mixins import UserPassesTestMixin  ##this will restrict user to change others post
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.



'''
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
'''

class PostListView(ListView):          #within list view we have to create a variable model
    model = Post                        # and this will tell out listview that which model we need to query in order to create list
    template_name = 'blog/home.html'     #creating new Template so that we can use our existing template
    #<app_name>/<model>_<viewtype>.html
    context_object_name = 'posts'       #in this we dont have to pass context

    #changing the order of post
    ordering = ['-date_posted']
    paginate_by = 5                     # means 5 posts will be visible only on the page. We are doing pagination


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'            #<app_name>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']   no need of this ..... This will be overwridden
    paginate_by = 5

    def get_queryset(self):       ## we will create our own url at run time
        user = get_object_or_404(User, username = self.kwargs.get('username'))  # we will get username from the url and kwargs is qwery parameters
        return Post.objects.filter(author = user).order_by('-date_posted')

###Making this fully default class
class PostDetailView(DetailView):
    model = Post



#for this the django will not expect post_create instead here it will expect post_form.html....it will club with update
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    ##this method ensures that the person who is writing the post is the current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    ##this method ensures that the person who is writing the post is the current user
    def form_valid(self, form):             #pre defined method
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):                    #pre defined method   #for TestMixIn
        post = self.get_object()
        #check if the current user is the author of the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'           #to redirect where we want to send user when the post is deleted

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def start(request):
    return render(request, 'blog/index.html')

## WE will create class based view.... THis will handle a lot of functionality at the backend itself