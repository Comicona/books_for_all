from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from references import models, forms


class AuthorsList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_authors'
    model = models.Author
    template_name = 'references/list_authors.html'
    

class GenresList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_genres'
    model = models.Genre
    template_name = 'references/list_genres.html'
    

class SeriesList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_series'
    model = models.Series
    template_name = 'references/list_series.html'


class PublishersList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_publishers'
    model = models.Publisher
    template_name = 'references/list_publishers.html'


class CategoriesList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_categories'
    model = models.Category
    template_name = 'references/list_categories.html'


class FormatsList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 10
    login_url = reverse_lazy('login')
    permission_required = 'references.view_formats'
    model = models.Format
    template_name = 'references/list_formats.html'


# references generic.DeleteViews
class AuthorDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_author'
    model = models.Author
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('authors')


class GenreDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_genre'
    model = models.Genre
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('genres')


class SeriesDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_series'
    model = models.Series
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('series')


class PublisherDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_publisher'
    model = models.Publisher
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('publishers')


class CategoryDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_category'
    model = models.Category
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('categories')


class FormatDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'references.delete_format'
    model = models.Format
    template_name = 'references/form_confirm_delete.html'
    success_url = reverse_lazy('formats')


# references UpdateViews
class AuthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_author'
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors')


class GenreUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_genre'
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres')


class SeriesUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series')


class PublisherUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_publisher'
    model = models.Publisher
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers')


class CategoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_category'
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('categories')


class FormatUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.change_format'
    model = models.Format
    form_class = forms.FormatForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('formats')


# references CreateViews
class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_author'
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('authors')


class GenreCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_genre'
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('genres')


class SeriesCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_series'
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('series')


class PublisherCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_publisher'
    model = models.Publisher
    form_class = forms.PublisherForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('publishers')


class CategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_category'
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('categories')


class FormatCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'references.add_bookformat'
    model = models.Format
    form_class = forms.FormatForm
    template_name = 'references/form_create_update.html'
    success_url = reverse_lazy('formats')