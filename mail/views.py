from django.views.generic import CreateView

from .models import Mail
from .forms import MailForm


class MailView(CreateView):
    model = Mail
    form_class = MailForm
    success_url = "/"
