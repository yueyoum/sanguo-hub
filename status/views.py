
# import arrow

import datetime

from django.views.generic import TemplateView
from django.db.models import Sum
from django.utils import timezone

from apps.server.models import Server
from apps.account.models import Account
from apps.character.models import Character
from apps.purchase.models import Purchase91Log

class StatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        servers = Server.objects.all()
        for s in servers:
            s.players_amount = Character.objects.filter(server_id=s.id).count()

        player = {}
        player['total_amount'] = Account.objects.count()

        # hours_24_before = arrow.utcnow().replace(days=-1)
        hours_24_before = timezone.now() - datetime.timedelta(days=1)
        player['new_24'] = Account.objects.filter(register_at__gte=hours_24_before).count()
        player['login_24'] = Account.objects.filter(last_login__gte=hours_24_before).count()


        purchase_server_info = []
        for s in servers:
            this_purchase_obj = Purchase91Log.objects.filter(server_id=s.id)
            this_server_purchase = {
                'id': s.id,
                'name': s.name,
                'purchase_total': this_purchase_obj.aggregate(Sum('order_money'))['order_money__sum'],
                'order_success_total': this_purchase_obj.filter(pay_status=1).count(),
                'order_failure_total': this_purchase_obj.filter(pay_status=0).count(),
                'order_unconfirmed_total': this_purchase_obj.filter(pay_status=-1).count(),

                'order_new_24': this_purchase_obj.filter(order_time__gte=hours_24_before).count(),
                'purchase_new_24': this_purchase_obj.filter(order_time__gte=hours_24_before).aggregate(Sum('order_money'))['order_money__sum'],
            }

            purchase_server_info.append(this_server_purchase)

        purchase_server_info.sort(key=lambda item: item['purchase_total'])


        purchase_char_info = []
        for p in Purchase91Log.objects.raw(
                "select id, server_id, char_id, sum(order_money) as sum_order_money from %s group by char_id order by sum_order_money desc limit 10" % Purchase91Log._meta.db_table
        ):
            purchase_server_info.append({
                'char_id': p.char_id,
                'server_id': p.server_id,
                'sum_order_money': p.sum_order_money
            })

        return {
            'servers': servers,
            'player': player,
            'order_total': Purchase91Log.objects.count(),
            'purchase_total': Purchase91Log.objects.aggregate(Sum('order_money'))['order_money__sum'],
            'purchase_server_info': purchase_server_info,
            'purchase_char_info': purchase_char_info,
        }
