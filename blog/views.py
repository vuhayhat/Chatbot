from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Post, User
from django.utils.text import slugify
from .forms import CommentForm, PostForm, EditProfileForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, approved=True).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "create_post.html"
    paginate_by = 6


class CreatePostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'the post has successfully created')
            return redirect('home')
        return render(request, 'create_post.html', {'form': form})


class ViewPost(generic.ListView):
    template_name = "view_post.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user, status=1).order_by("-created_on")
    

class UpdatePostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(instance=post)
        return render(request, 'update_post.html', {'form': form, 'post': post})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post')
        return render(request, 'update_post.html', {'form': form, 'post': post})

    def form_valid(self, form):
        
        form.instance.approved = False
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class DeletePostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        return render(request, 'delete_post_confirm.html', {'post': post})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        post.delete()
        return redirect('view_post')


class EditProfileView(LoginRequiredMixin, View):
    login_url = 'account_login'
    template_name = 'show_profile.html'

    def get(self, request):
        edit_profile_form = EditProfileForm(instance=request.user)
        return render(request, self.template_name, {'edit_profile_form': edit_profile_form})

    def post(self, request):
        edit_profile_form = EditProfileForm(request.POST, instance=request.user)
        if edit_profile_form.is_valid():
            first_name = edit_profile_form.cleaned_data.get('first_name')
            last_name = edit_profile_form.cleaned_data.get('last_name')
            email = edit_profile_form.cleaned_data.get('email')
            
            if not first_name or not last_name or not email:
                messages.error(request, 'please fill all')
                return redirect('show_profile')
            
            edit_profile_form.save()
            messages.success(request, 'your profile has been successfully edited')
            return redirect('home')
        return render(request, self.template_name, {'edit_profile_form': edit_profile_form})


@login_required
def show_profile(request):
    edit_profile_form = EditProfileForm(instance=request.user)

    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, instance=request.user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('home')

    return render(
        request,
        'show_profile.html',
        {'edit_profile_form': edit_profile_form}
    )