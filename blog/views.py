from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from .forms import CommentEditForm,CommentForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import email_confirmation_required
from django.views.decorators.cache import cache_control

def home(request,id):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/blog_home.html',context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/blog_home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
@email_confirmation_required
def post_detail(request,id):
	post_obj = get_object_or_404(Post, id = id)
	comments = post_obj.comments.filter(parent__isnull=True)
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			parent_obj = None
			try:
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
			if parent_id:
				parent_obj = Comment.objects.get(id=parent_id)
				if parent_obj:
					replay_comment = Comment()
					replay_comment.post_id = post_obj
					replay_comment.author = request.user
					replay_comment.text = comment_form.cleaned_data['body']
					replay_comment.parent = parent_obj
					replay_comment.save()
					return redirect('/post/'+str(id)+'/')
			new_comment = Comment()
			new_comment.post_id = post_obj
			new_comment.author = request.user
			new_comment.text = comment_form.cleaned_data['body']
			new_comment.save()
			return redirect('/post/'+str(id)+'/')
	else:
		comment_form = CommentForm()
	context = {'post': post_obj,'comments': comments,'comment_form': comment_form}
	return render(request,'blog/post_detail.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
@email_confirmation_required
def EditComment(request,pid,cid):
	post1 = Post.objects.get(id=pid)
	comment = Comment.objects.get(id=cid)
	
	form = CommentEditForm()
	if request.method == 'POST':
		form = CommentEditForm(request.POST)
		if form.is_valid():
			comment.text = form.cleaned_data['text']
			comment.author = request.user
			comment.post_id = post1
			comment.save()
			
			return redirect('/post/'+str(pid)+'/')
	return render(request, 'blog/edit-comment.html', {'form':form})
	
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
@email_confirmation_required
def DeleteComment(request,pid,cid):
	post1 = Post.objects.get(id=pid)
	comment = Comment.objects.get(id=cid)
	if comment:
		comment.delete()
		return redirect('/post/'+str(pid)+'/')
	return render(request, 'blog/edit-comment.html')

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
	model = Post
	fields = ['title','content']
	ordering = ['-date_posted']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
	model = Post
	success_url = '/blog'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




