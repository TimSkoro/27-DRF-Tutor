from django.contrib.auth.models import User


class Moderator(User):

    class Meta:
        proxy = True
        permissions = [('can_enjoi_news', 'Can take enjoi')]