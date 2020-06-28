from dal import autocomplete
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from core.forms import MixForm, MyUserCreationForm, SigninForm
from core.models import Mix, Group, Tag, MyUser


class MixCreateView(LoginRequiredMixin, CreateView):
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


class MixEditView(LoginRequiredMixin, UpdateView):
    model = Mix
    form_class = MixForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroupView(LoginRequiredMixin, DetailView):
    model = Group


class MixView(LoginRequiredMixin, DetailView):
    model = Mix


class GroupListView(LoginRequiredMixin, ListView):
    model = Group


class TagView(LoginRequiredMixin, DetailView):
    model = Tag


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.extra(select={'lower_title': 'lower(title)'}).order_by('lower_title')

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs


def home(request):
    regform = MyUserCreationForm()
    signinform = SigninForm()
    if request.user.is_authenticated:
        if request.user.the_group:
            return redirect(request.user.the_group.get_absolute_url())
        elif hasattr(request.user, 'mix'):
            return redirect(request.user.mix.get_absolute_url())
        else:
            return redirect('mixcreate')

    if request.method == 'POST':
        regform = MyUserCreationForm(request.POST)
        if regform.is_valid():
            data = regform.cleaned_data
            valid = True
            if MyUser.objects.filter(username=data['username']):
                regform.add_error('username', 'We already have a user with this email!')
                valid = False
            if MyUser.objects.filter(mefi_handle=data['mefi_handle']):
                regform.add_error('mefi_handle', 'We already have a user with this MeFi username!')
                valid = False
            if valid:
                user = MyUser(
                    username=data['username'],
                    mefi_handle=data['mefi_handle'],
                    platform=data['platform'],
                )
                user.set_password(data['password1'])
                user.save()
                login(request, user)
                return redirect('mixcreate')

    return render(request, 'core/home.html', locals())
