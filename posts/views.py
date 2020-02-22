from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    #return HttpResponse("Hello World!")

    posts = Post.objects.order_by('-published') #asc

    #return render(request, 'posts/index.html')
    # viewsからtemplatesに値を渡したい場合。
    # データはmodel経由で渡されるので、postモデルをインポートして、それをview経由でtemplateへ渡す
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request,post_id):
    #post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'posts/post_detail.html', {'post':post})
# Create your views here.
