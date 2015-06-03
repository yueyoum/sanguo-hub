# -*- coding: utf-8 -*-

import json
import arrow

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView
from django.db.models import Sum, Q

from apps.server.models import Server
from apps.account.models import Account
from apps.purchase.models import (
    PurchaseJodoPlayLog,
    PurchaseAiyingyongLog,
)

FORMAT = "YYYY-MM-DD HH:mm:ssZ"


class StatusView(TemplateView):
    template_name = 'status.html'

@csrf_exempt
def status_ajax(request):
    date1 = "%s 00:00:00" % request.POST['date1']
    date2 = "%s 00:00:00" % request.POST['date2']

    date1 = arrow.get(date1).replace(tzinfo=settings.TIME_ZONE)
    date2 = arrow.get(date2).replace(tzinfo=settings.TIME_ZONE)

    # 日新增用户
    rixinzengyonghu = []
    # 日充值用户
    richongzhiyonghu = []
    # 日充值金额
    richongzhijine = []

    day_start = date1

    while(True):
        if day_start > date2:
            break

        day_end = day_start.replace(days=1)

        date_str = day_start.format("YYYY-MM-DD")
        condition = Q(register_at__gte=day_start.format(FORMAT)) & Q(register_at__lte=day_end.format(FORMAT))

        rixinzengyonghu.append({
            'date': date_str,
            'value': Account.objects.filter(condition).count()
        })

        if settings.STATUS_PLATFORM == 'jodo':
            condition = Q(order_time__gte=day_start.format(FORMAT)) & Q(order_time__lte=day_end.format(FORMAT))
            richongzhiyonghu.append({
                'date': date_str,
                'value': PurchaseJodoPlayLog.objects.filter(condition).count()
            })

            money = PurchaseJodoPlayLog.objects.filter(condition).aggregate(Sum('jodo_price'))['jodo_price__sum']
            money = money / 5 if money else 0

            richongzhijine.append({
                'date': date_str,
                'value': money
            })
        elif settings.STATUS_PLATFORM == 'aiyingyong':
            condition = Q(order_time__gte=day_start.format(FORMAT)) & Q(order_time__lte=day_end.format(FORMAT))
            richongzhiyonghu.append({
                'date': date_str,
                'value': PurchaseAiyingyongLog.objects.filter((condition)).count()
            })

            money = PurchaseAiyingyongLog.objects.filter(condition).aggregate(Sum('order_money'))['order_money__sum']
            money = money if money else 0

            richongzhijine.append({
                'date': date_str,
                'value': money
            })


        day_start = day_end


    data = {
        'rixinzengyonghu': rixinzengyonghu,
        'richongzhiyonghu': richongzhiyonghu,
        'richongzhijine': richongzhijine
    }

    return HttpResponse(json.dumps(data), content_type='application/json')

