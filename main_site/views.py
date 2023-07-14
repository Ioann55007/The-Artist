from django.shortcuts import render
from django.views import View


def first_page(request):
    return render(request, 'first_page.html')


class AboutView(View):

    @staticmethod
    def get(request):
        return render(request, template_name='about_me.html')


class DeliverView(View):

    @staticmethod
    def get(request):
        return render(request, template_name='deliver.html')


class Confiden(View):

    @staticmethod
    def get(request):
        return render(request, template_name='confiden.html')



