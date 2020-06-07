from dal import autocomplete
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from core.forms import MixForm, MyUserCreationForm, SigninForm
from core.models import Mix, Group, Tag


class MixCreateView(CreateView):
    model = Mix
    form_class = MixForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = None
        if hasattr(request.user, 'mix'):
            return redirect('mixedit', pk=request.user.mix.id)
        return super().get(request, *args, **kwargs)


class MixEditView(UpdateView):
    model = Mix
    form_class = MixForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupView(DetailView):
    model = Group


class MixView(DetailView):
    model = Mix


class GroupListView(ListView):
    model = Group


class TagView(DetailView):
    model = Tag


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs

def home(request):
    regform = MyUserCreationForm()
    signinform = SigninForm()
    return render(request, 'core/home.html', locals())