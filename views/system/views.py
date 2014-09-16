# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-8-26'

import json

from django.shortcuts import render_to_response
from django.http import HttpResponse

from apps.system.models import BulletinConfig, Bulletin, Broadcast


def get_bulletins(request):
    ret_json = request.GET.get('format', '') == 'json'
    config = BulletinConfig.objects.all()[0]

    width = request.GET.get('width', '')
    if not width:
        width = config.window_width

    context = {
        'width': width,
        'margin': config.window_margin,
        'image_width': int(width) - config.window_margin * 2 if width else '',
        'radius': config.bulletin_window_border_radius,
        'window_bg_color': config.window_bg_color,
        'window_bg_image': config.window_bg_image.url if config.window_bg_image else '',

        'title_size': config.bulletin_title_size,
        'content_size': config.bulletin_content_size,
    }


    def _get_real_value(obj, obj_file_name, config_file_name, is_filefield=False):
        value = getattr(obj, obj_file_name)
        if not value:
            value = getattr(config, config_file_name)

        if is_filefield:
            if value:
                return value.url
            return ""
        return value

    bulletins = []

    for b in Bulletin.objects.filter(display=True).order_by('-order_seq', '-create_time'):
        data = {
            'title': b.title,
            'title_color': _get_real_value(b, 'title_color', 'bulletin_title_color'),
            'title_bg_color': _get_real_value(b, 'title_bg_color', 'bulletin_title_bg_color'),
            'title_bg_image': _get_real_value(b, 'title_bg_image', 'bulletin_title_bg_image', True),

            'content': b.content.replace('\r\n', '<br />'),
            'content_color': _get_real_value(b, 'content_color', 'bulletin_content_color'),
            'content_bg_color': _get_real_value(b, 'content_bg_color', 'bulletin_content_bg_color'),
            'content_bg_image': _get_real_value(b, 'content_bg_image', 'bulletin_content_bg_image', True),

            'content_image': b.content_image.url if b.content_image else "",
        }

        bulletins.append(data)

    context['bulletins'] = bulletins

    if ret_json:
        return HttpResponse(json.dumps(context), content_type='application/json')

    return render_to_response('bulletin.html', context)


def get_broadcast(request):
    b = Broadcast.objects.all()
    if b.count() > 0:
        content = b[0].content
    else:
        content = u""

    data = {
        'ret': 0,
        'data': content
    }

    return HttpResponse(json.dumps(data), content_type='application/json')
