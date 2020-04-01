from django.shortcuts import render,HttpResponse
from blog.models import Post
from django.core.paginator import Paginator
# Create your views here.
def bloghome(request):
    allPosts=Post.objects.all()

    paginator=Paginator(allPosts,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        allPosts=paginator.page(page)
    except(EmptyPage,InvalidPage):
        allPosts=paginator=paginator.page(paginator.num_pages)

    content={'allPosts':allPosts}
    return render(request,'blog/bloghome.html',content)
    # return HttpResponse('This is blog Home')


def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first
    content={'post':post}
    return render(request,'blog/blogpost.html',content)
#    return HttpResponse(f'This is Blogpost slug {slug}' )