from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .forms import ProfileForm
from .serializers import ProfileSerializer


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

    def get_success_url(self):
        return reverse('profile', kwargs={"pk": self.object.id})


class DeleteProfile(DeleteView):
    model = Profile
    success_url = reverse_lazy("first")

   


class ProfileApi(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Метод PUT не разрешён"})

        try:
            instance = Profile.objects.get(pk=pk)
        except:
            return Response({"error": "Объект не найден"})

        serializer = ProfileSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
