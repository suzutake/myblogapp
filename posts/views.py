from django.shortcuts import render
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
    print(post_id)
    return render(request, 'posts/post_detail.html', {'post_id':post_id})
# Create your views here.
