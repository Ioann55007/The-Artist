from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, DetailView
from rest_framework import permissions
from rest_framework.permissions import BasePermission

from .models import Profile
from .forms import ProfileForm




class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["profiles"] = profile
        return context


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_user/profile_form.html'

    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse('profile', kwargs={"pk": self.object.id})
