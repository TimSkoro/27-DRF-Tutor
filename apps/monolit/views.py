from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home_page.html'
