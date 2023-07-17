from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import ReviewForm
from .models import Picture, Review, Viewer


class ViewPicture(ListView):
    model = Picture
    queryset = Picture.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = Picture.objects.last()
        context['pictures'] = pictures
        return context



class CountViewerMixin:

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if hasattr(self.object, 'views'):
            viewer, created = Viewer.objects.get_or_create(
                ipaddress=None if request.user.is_authenticated else get_client_ip(request, id),
                user=request.user if request.user.is_authenticated else None
            )

            if self.object.views.filter(id=viewer.id).count() == 0:
                self.object.views.add(viewer)

        return response


class DetailPicture(CountViewerMixin, FormMixin, DetailView):
    model = Picture
    template_name = 'pictures/picture_detail.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        liked = False
        if self.object.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['picture'] = context.get('object')
        context['liked'] = liked

        return context

    def post(self, request, slug, *args, **kwargs):
        picture = get_object_or_404(Picture, slug=slug)
        reviews = Review.objects.all()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = self.request.user
                form.picture = picture
                form.save()
                # return redirect('pictures:picture', pk)
        else:
            form = ReviewForm()
        return render(request, 'pictures/picture_detail.html', {'form': form, 'reviews': reviews, 'picture': picture,
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
        picture = Picture.objects.get(id=id)
        if picture.likes.filter(id=request.user.id).exists():
            picture.likes.remove(request.user.id)
        else:
            picture.likes.add(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
