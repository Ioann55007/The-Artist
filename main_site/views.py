from django.shortcuts import render
from django.views import View




def first_page(request):
    return render(request, 'first_page.html')


class AboutView(View):

    def get(self, request):
        return render(request, template_name='about_me.html')


class DeliverView(View):

    @staticmethod
    def get(request):
        return render(request, template_name='deliver.html')




