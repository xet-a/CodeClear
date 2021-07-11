from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Avg

from .models import Closet
from .forms import ClosetCreateForm


def index(request):

    clothes_list = Closet.objects.all().order_by('put_date')
    num = Closet.objects.count()
    context = {'clothes_list': clothes_list, 'num':num}

    return render(request, 'shop/clothes_list.html', context)



def closet_create(request):
    if request.method == 'POST':
        form = ClosetCreateForm()
        if form.is_valid():
            context = form.save(commit=False)
            context.create_date = timezone.now()
            context.save()
            return redirect('shop:index')

    else:
        form = ClosetCreateForm()
    content = {'form': form}

    return render(request, 'shop/closetCreate_form.html', content)