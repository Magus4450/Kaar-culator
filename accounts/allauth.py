from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy


class AccountAdapter(DefaultAccountAdapter):

  def get_login_redirect_url(self, request):
      return reverse_lazy('home:home')