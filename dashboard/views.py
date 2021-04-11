from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['products'] = context['products'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        context['products'] = context['products'].filter(
            is_available=True)

        return context
