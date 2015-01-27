# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/23/14'

from django.db.models import Q

import arrow

from apps.activatecode.models import ActivateCode, ActivateCodeUseLog
from preset import errormsg

def use(char_id, code_id):
    # EXIST ?
    try:
        ac = ActivateCode.objects.select_related('bucket').get(code_id=code_id)
    except ActivateCode.DoesNotExist:
        return {'ret': errormsg.ACTIVATE_CODE_NOT_EXIST}

    # CAN USE ?
    if not ac.bucket.can_use:
        return {'ret': errormsg.ACTIVATE_CODE_CAN_NOT_USE}

    # DATE LIMIT
    if ac.bucket.has_date_limit:
        now_date = arrow.utcnow().date()
        print now_date
        print ac.bucket.active_start
        print ac.bucket.active_end
        if now_date < ac.bucket.active_start:
            return {'ret': errormsg.ACTIVATE_CODE_NOT_START}
        if now_date > ac.bucket.active_end:
            return {'ret': errormsg.ACTIVATE_CODE_EXPIRED}

    # ALREADY USED BY THIS CHAR ?
    if ActivateCodeUseLog.objects.filter(Q(code_id=code_id) & Q(char_id=char_id)).exists():
        return {'ret': errormsg.ACTIVATE_CODE_ALREADY_USED}

    # 同类也不能多次使用
    used_codes = ActivateCodeUseLog.objects.filter(char_id=char_id).values_list('code_id', flat=True)
    used_codes = list(used_codes)
    used_bucket_ids = ActivateCode.objects.filter(code_id__in=used_codes).values_list('bucket', flat=True)
    this_code_bucket_id = ac.bucket.id
    if this_code_bucket_id in used_bucket_ids:
        return {'ret': errormsg.ACTIVATE_CODE_ALREADY_USED}

    # USED TIMES LIMITS ?
    if ac.bucket.use_times_limit > 0:
        used_times = ActivateCodeUseLog.objects.filter(code_id=code_id).count()
        if used_times >= ac.bucket.use_times_limit:
            return {'ret': errormsg.ACTIVATE_CODE_USED_TIMES_OUT}

    # ALL OK
    package = ac.bucket.package.export_data()
    ActivateCodeUseLog.objects.create(code_id=code_id, char_id=char_id)

    return {
        'ret': 0,
        'data': {
            'package': package
        }
    }
