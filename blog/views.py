from django.views import generic
from .models import Post, About, Category, Comment
from .forms import CommentForm, PostSearchForm
from django.shortcuts import render, get_object_or_404, redirect
from taggit.models import Tag

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    slug = Category.objects.all()
    paginate_by = 5
    
    def get_context_data(self, *args,**kwargs):
        cats = Category.objects.all()
        context = super(PostList, self).get_context_data(*args,**kwargs)
        context["cats"] = cats
        return context




def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    tags = Tag.objects.all()
    new_comment = None
    comment_form = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            
        else:
            comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            'tags':tags
        },
    )


class TagIndexView(generic.ListView):
    model = Post
    template_name = "tags.html"
     

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))




def aboutus(request):
    obj = About.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'about.html', context)


def aboutussidebar(request):
    obj = About.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'sidebar.html', context)


def post_search(request):
    form = PostSearchForm()
    tags = Tag.objects.all()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(title__contains=q)


    return render(request, "search.html",{'form':form,
    'q':q,
    'results':results,
    'tags':tags})


def category(request, slug):
    category = Category.objects.get(slug=slug)
    category_posts = Post.objects.filter(category__name=slug)
    tags = Tag.objects.all()

    context = {
        'category':category,
        'category_posts':category_posts,
        'tags':tags

    }
    return render(request, 'category.html', context)


# handling reply, reply view
