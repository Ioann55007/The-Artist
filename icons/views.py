from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from rest_framework.response import Response

from .forms import ReviewForm
from .models import Icon, Review, Viewer
from rest_framework.views import APIView

from .serializers import IconDetailSerializer, IconCreateSerializer


class ViewIcon(ListView):
    model = Icon
    # queryset = Icon.objects.all()
    et = Icon.objects.all()
    template_name = 'icon_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['icons'] = Icon.objects.all()
        return context


class CountViewerMixin:

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if hasattr(self.object, 'viewers'):
            viewer, created = Viewer.objects.get_or_create(
                ipaddress=None if request.user.is_authenticated else get_client_ip(request, id),
                user=request.user if request.user.is_authenticated else None
            )

            if self.object.viewers.filter(id=viewer.id).count() == 0:
                self.object.viewers.add(viewer)

        return response


class DetailIcon(CountViewerMixin, FormMixin, DetailView):
    model = Icon
    template_name = 'icon_detail.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        liked = False
        if self.object.icon_likes.filter(id=self.request.user.id).exists():
            liked = True
        context['icon'] = context.get('object')
        context['liked'] = liked

        return context

    def post(self, request, slug, *args, **kwargs):
        icon = get_object_or_404(Icon, slug=slug)
        reviews = Review.objects.all()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = self.request.user
                form.icon = icon
                form.save()
        else:
            form = ReviewForm()
        return render(request, 'icon_detail.html', {'form': form, 'reviews': reviews, 'icon': icon,
                                                    })


def get_client_ip(request, id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def delete_review(request, id):
    review = Review.objects.get(id=id)
    if review.author == request.user:
        review.is_removed = True
        review.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def like(request, id):
    if request.method == 'POST':

        icon = Icon.objects.get(id=id)

        if icon.icon_likes.filter(id=request.user.id).exists():
            icon.icon_likes.remove(request.user.id)
        else:
            icon.icon_likes.add(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




class IconDetailView(APIView):
    def get(self, request):
        icon = Icon.objects.filter(name__startswith="Царь Давид")
        serializer = IconDetailSerializer(icon, many=True)
        return Response({'icon': serializer.data})


class IconCreateView(APIView):

    def get(self, request):
        icon_list = Icon.objects.all()
        return Response({"icons": IconCreateSerializer(icon_list, many=True).data})

    def post(self, request):
        icon = IconCreateSerializer(data=request.data)
        if icon.is_valid():
            icon.save()
        return Response(status=201)



