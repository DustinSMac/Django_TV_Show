from django.shortcuts import render, redirect
from .models import show

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context={
        'all_shows': show.objects.all(),
    }
    return render(request,"index.html",context)

def new(request):
    return render(request,"new.html")

def newShow(request):
    newS=show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
        )
    return redirect(f'/shows/{newS.id}')

def ShowPage(request,show_id):
    shows=show.objects.get(id=show_id)
    context={
        'show': shows,
    }
    return render(request,"show.html", context)

def EditShow(request,show_id):
    eShow=show.objects.get(id=show_id)
    context={
        'show': eShow,
    }
    return render(request,"edit.html",context)

def editShowPage(request,show_id):
    editShow=show.objects.get(id=show_id)
    editShow.title=request.POST['title']
    editShow.network=request.POST['network']
    editShow.release_date=request.POST['release_date']
    editShow.description=request.POST['description']
    editShow.save()
    return redirect(f'/shows/{editShow.id}')

def DeleteShow(request,show_id):
    dShow=show.objects.get(id=show_id)
    dShow.delete()
    return redirect('/')
    