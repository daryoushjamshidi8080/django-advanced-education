from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, TemplateView, RedirectView, FormView, ListView
from  .models import Post
from .forms import ContactForm
from django.urls import reverse_lazy


def IndexViews(request):
    """
    a function based view to show index page
    """
    return render(request, 'index.html')






class IndexView(TemplateView):
    """
        a class based view to show index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['firstname'] = 'dyaus'
        context['lastname'] = 'jamshidi'
        context['posts'] = Post.objects.all()
        return context



class MyRedirectView(RedirectView):
    """
        redirect a page with  class redirectView
    """

    pattern_name = 'blog:home'
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])

        print(post)

        return super().get_redirect_url(*args)




class PostList(ListView):
    """
     a class for display posts
    """

    # model = Post #specify the model for list view
    # queryset = Post.objects.all()

    context_object_name = 'posts'
    paginate_by = 2
    # ordering = '-id' 


    def get_queryset(self) -> QuerySet[Any, Any]:
        posts = Post.objects.filter(status=True).order_by('id')
        return posts 


class PostCreateView(FormView):
    """
        a class 
    """
    template_name = "blog/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("blog:post-list")
    
