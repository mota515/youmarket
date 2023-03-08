from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Goods
from .forms import GoodsForm
# Create your views here.


class IndexView(ListView):
    model = Goods
    template_name = 'youmarket/index.html'
    context_object_name = 'goodss'
    paginate_by = 2
    ordering = ['-dt_created']

class GoodsCreateView(CreateView):
    model = Goods
    form_class = GoodsForm
    template_name = 'youmarket/goods_form.html'

    def get_success_url(self):
        return reverse("index")
# def index(request):
#     return render(request, 'youmarket/index.html')
