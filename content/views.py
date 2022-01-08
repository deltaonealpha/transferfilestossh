from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from .forms import ProfileForm
from .models import Movie,TvShow,Episode,termsconditionlisting,Ebook
from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from random import randint
# Create your views here.
#@method_decorator(login_required,name='dispatch')
class homeindex(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homeindex')
        else:
            aboutinfo = termsconditionlisting.objects.all()
            return render(request,'../templates/homepage.html',
                {
                    'aboutinfo':aboutinfo,
                })
class ShowMovie(View):
    def get(self,request,*args, **kwargs):
        latestmovie10 = Movie.objects.filter(displayornot=True).order_by('-releasedate')[:10]
        popular10 = Movie.objects.filter(displayornot=True).order_by('-views')[:10]
        tvpopular10 = TvShow.objects.filter(displayornot=True).order_by('-views')[:10]
        headermovie = Movie.objects.filter(displayornot=True).latest('releasedate')
        count = Movie.objects.aggregate(count=Count('id'))['count']
        tv_count = TvShow.objects.aggregate(count=Count('id'))['count']
        ebook10 = Ebook.objects.filter(displayornot=True).order_by('-title')[:10]
        random_index = 7
        try:
            randommovie = Movie.objects.get(pk=random_index)
        except:
            random_index = 7
            randommovie = Movie.objects.get(pk=random_index)
        tv_random_index = 3
        try:
            randomtv = TvShow.objects.get(pk=tv_random_index)
        except:
            tv_random_index = 3
            randomtv = TvShow.objects.get(pk=tv_random_index)
        try:
            randomtv10 = TvShow.objects.get(pk=tv_random_index).episodes.order_by('episode_num')[:3]
        except:
            randomtv10 = TvShow.objects.get(pk=tv_random_index).episodes.order_by('episode_num')
        print(randomtv10)
        return render(request,'../templates/homeindex.html',{
        'latestmovie10':latestmovie10,
        'headermovie':headermovie,
        'popular10':popular10,
        'randommovie':randommovie,
        'randomtv': randomtv,
        'randomtv10':randomtv10,
        'ebook10': ebook10,
        'tvpopular10': tvpopular10,
        })
class PlayMovie(View):
    def get(self,request,id):
        obj = Movie.objects.get(pk=id)
        print(obj.views)
        obj.views = obj.views + 1  
        obj.save()
        if request.user.is_authenticated:
            return render(request,'../templates/play.html',{
        'movie':obj,
        })
        else:
            return redirect("homepageintro")
class PlayTv(View):
    def get(self,request,id):
        objmain = TvShow.objects.get(pk=id)
        obj = TvShow.objects.get(pk=id).episodes.order_by('episode_num')
        return render(request,'../templates/listepisode.html',{
        'objmain':objmain,
        'episodes':obj,
        })
class ReadEbook(View):
    def get(self,request,id):
        objmain = Ebook.objects.get(pk=id)
        return render(request,'../templates/read.html',{
        'objmain':objmain,
        })
class PlayEpTv(View):
    def get(self,request,id1,id2):
        objmain = TvShow.objects.get(pk=id1).episodes.get(pk=id2)
        if request.user.is_authenticated:
            return render(request,'../templates/playtv.html',{
        'movie':objmain,
        })
        else:
            return redirect("homepageintro")
def ListAllMovie(request):
    user_list = Movie.objects.filter(displayornot=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, '../templates/listallmovies.html', { 'movie': users })
def ListWhatsnEw(request):
    user_list = Movie.objects.filter(displayornot=True).order_by('-releasedate')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 16)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, '../templates/whatsnew.html', { 'movie': users })        
def ListAllEbooks(request):
    user_list = Ebook.objects.filter(displayornot=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, '../templates/listallebooks.html', { 'movie': users })
def ListAllTv(request):
    user_list = TvShow.objects.filter(displayornot=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, '../templates/listalltv.html', { 'movie': users })
class ShowTVShow(View):
    def get(self,request,*args, **kwargs):
        latestmovie10 = TvShow.objects.filter(displayornot=True).order_by('-releasedate')[:10]
        headermovie = TvShow.objects.filter(displayornot=True).latest('releasedate')
        return render(request,'../templates/homeindex.html',{
        'latestmovie10':latestmovie10,
        'headermovie':headermovie,
        })
class aboutlisting(View):
    def get(self,request,*args, **kwargs):
        aboutinfo = termsconditionlisting.objects.all()
        return render(request,'../templates/about.html',{
        'aboutinfo':aboutinfo,
        })
class termlisting(View):
    def get(self,request,*args, **kwargs):
        aboutinfo = termsconditionlisting.objects.all()
        return render(request,'../templates/term.html',{
        'aboutinfo':aboutinfo,
        })
class privacypolicylisting(View):
    def get(self,request,*args, **kwargs):
        aboutinfo = termsconditionlisting.objects.all()
        return render(request,'../templates/privacypolicy.html',{
        'aboutinfo':aboutinfo,
        })
class faqlisting(View):
    def get(self,request,*args, **kwargs):
        aboutinfo = termsconditionlisting.objects.all()
        return render(request,'../templates/faq.html',{
        'aboutinfo':aboutinfo,
        })
class profileview(View):
    def get(self,request,*args, **kwargs):
        aboutinfo = termsconditionlisting.objects.all()
        if request.user.is_authenticated :
            return render(request,'../templates/profile.html',{
        'aboutinfo':aboutinfo,
        })
        else:
            return redirect("homepageintro")
from itertools import chain
def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            pr1 = Movie.objects.filter(title=query_name)
            pr2 = TvShow.objects.filter(title=query_name)
            results = list(chain(pr1,pr2))
            return render(request, '../templates/search.html', {"results":results})
    return render(request, '../templates/search.html')