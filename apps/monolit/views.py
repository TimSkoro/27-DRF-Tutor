from django.views.generic import TemplateView

def f():
    pass

class HomePage(TemplateView):
    template_name = 'home_page.html'
