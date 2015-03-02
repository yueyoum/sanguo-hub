# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.system.models import Bulletin, BulletinConfig, Broadcast


class BulletinConfigAdmin(admin.ModelAdmin):
    list_display = (
        'window_width', 'window_margin',
        'window_bg_color', 'WindowBgImage',
        'bulletin_window_border_radius',

        'bulletin_title_size', 'bulletin_title_color',
        'bulletin_title_bg_color', 'BulletinTitleBgImage',

        'bulletin_content_size', 'bulletin_content_color',
        'bulletin_content_bg_color', 'BulletinContentBgImage',
    )

    def WindowBgImage(self, obj):
        if not obj.window_bg_image:
            return ""

        return u'<a href="{0}" target=_blank>显示图片</a>'.format(obj.window_bg_image.url)
    WindowBgImage.allow_tags = True
    WindowBgImage.short_description = "窗口背景图片"

    def BulletinTitleBgImage(self, obj):
        if not obj.bulletin_title_bg_image:
            return ""

        return u'<a href="{0}" target=_blank>显示图片</a>'.format(obj.bulletin_title_bg_image.url)
    BulletinTitleBgImage.allow_tags = True
    BulletinTitleBgImage.short_description = "默认公告标题背景图片"

    def BulletinContentBgImage(self, obj):
        if not obj.bulletin_content_bg_image:
            return ""

        return u'<a href="{0}" target=_blank>显示图片</a>'.format(obj.bulletin_content_bg_image.url)
    BulletinContentBgImage.allow_tags = True
    BulletinContentBgImage.short_description = "默认公告内容背景图片"



class BulletinAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'ContentImage',
                    'order_seq', 'create_time',

                    'title_color', 'title_bg_color', 'TitleBgImage',
                    'content_color', 'content_bg_color', 'ContentBgImage',

                    'show_for_old_version', 'show_for_new_version',

    )

    ordering = ('-order_seq', '-create_time')

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'content_image', 'order_seq',
                        'show_for_old_version', 'show_for_new_version',
                        )
        }),
        ('高级', {
            'classes': ('collapse',),
            'fields': ('title_color', 'title_bg_color', 'title_bg_image',
                        'content_color', 'content_bg_color', 'content_bg_image',
            )
        })
    )

    def ContentImage(self, obj):
        if not obj.content_image:
            return ""

        return u'<a href="{0}" target=_blank>显示图片</a>'.format(obj.content_image.url)
    ContentImage.allow_tags = True
    ContentImage.short_description = "内容图片"


    def TitleBgImage(self, obj):
        if not obj.title_bg_image:
            return ""

        return u'<a href="{0}" target=_blank>显示图片</a>'.format(obj.title_bg_image.url)
    TitleBgImage.allow_tags = True
    TitleBgImage.short_description = "标题背景图片"

    def ContentBgImage(self, obj):
        if not obj.content_bg_image:
            return ""

        return u'<a href="{0}" target=_blank>显示图片</a>'.format(obj.content_bg_image.url)
    ContentBgImage.allow_tags = True
    ContentBgImage.short_description = "内容背景图片"



class BroadcastAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'play_times', 'active', 'start_at', 'end_at'
    )


admin.site.register(BulletinConfig, BulletinConfigAdmin)
admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(Broadcast, BroadcastAdmin)

