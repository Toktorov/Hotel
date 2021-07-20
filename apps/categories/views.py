from django.views import generic
from apps.categories.models import Category
from django.urls import reverse_lazy
from apps.categories.forms import CategoryForm


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category/index.html'
    paginate_by = 20
    context_object_name = 'categories'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('index_category')
    template_name = 'category/create.html'


class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('index_category')
    template_name = 'category/update.html'


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy('index_category')
    template_name = 'category/delete.html'