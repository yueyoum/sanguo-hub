
import json

from django.conf import settings
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.db.models import Sum, Count

from apps.server.models import Server
from apps.account.models import Account
from apps.character.models import Character
from apps.purchase.models import Purchase91Log


SHOW_PURCHASE_CHARS_AMOUNT = 20


class StatusView(TemplateView):
    template_name = 'status.html'


def status_ajax(request):
    print request.POST
    return HttpResponse(json.dumps({}), content_type='application/json')

