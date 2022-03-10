from django import template
from mail.forms import MailForm

register = template.Library()


@register.inclusion_tag("mail/tags/form.html")
def mail_form():
    return {"mail_form": MailForm()}