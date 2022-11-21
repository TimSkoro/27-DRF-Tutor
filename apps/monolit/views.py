from django.views.generic import TemplateView

from apps.monolit.models import News


class HomePage(TemplateView):
    template_name = 'home_page.html'


class NewsPage(TemplateView):
    template_name = 'news.html'

    def get(self, request, *args, **kwargs):
        context = {
            "some_list": News.objects.all(),
        }
        return self.render_to_response(context)


class ContactPage(TemplateView):
    template_name = 'contacts.html'
