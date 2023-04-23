from django.shortcuts import render

# Create your views here.
def home(request):
    # allPosts = Post.objects.filter(status=1).order_by('-created_on')
    # paginator = Paginator(allPosts, 5)
    # page = request.GET.get('page')
    # paged_posts = paginator.get_page(page)
    # context ={
    #     'allPosts': paged_posts,
    # }
    return render(request, 'main/home.html')