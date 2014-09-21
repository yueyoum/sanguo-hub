# -*-coding: utf-8 -*-

from django.db import models

from core.fixtures import RESOURCE_TYPE

class CheckInDate(models.Model):
    checkin_date = models.DateField("日期", db_index=True)

    class Meta:
        db_table = 'checkin_date'
        verbose_name = "签到"
        verbose_name_plural = "签到"

    def export_data(self):
        # {
        #   index_number: {
        #     'icons': [(icon_one_type, icon_one_id, icon_one_amount), ...],
        #     'package': package
        #   },
        #   ...
        # }
        items = self.checkin_items.all()
        data = {}
        for item in items:
            data[item.index_number] = {
                'icons': [
                    (item.icon_one_type, item.icon_one_id, item.icon_one_amount),
                    (item.icon_two_type, item.icon_two_id, item.icon_two_amount),
                    (item.icon_three_type, item.icon_three_id, item.icon_three_amount),
                ],
                'package': item.package.export_data()
            }

        return data


class CheckInItem(models.Model):
    checkin_date = models.ForeignKey(CheckInDate, related_name='checkin_items')
    index_number = models.IntegerField("序号")

    icon_one_type = models.IntegerField("类型", choices=RESOURCE_TYPE)
    icon_one_id = models.IntegerField("ID")
    icon_one_amount = models.IntegerField("数量", default=1)

    icon_two_type = models.IntegerField("类型", choices=RESOURCE_TYPE)
    icon_two_id = models.IntegerField("ID")
    icon_two_amount = models.IntegerField("数量", default=1)

    icon_three_type = models.IntegerField("类型", choices=RESOURCE_TYPE)
    icon_three_id = models.IntegerField("ID")
    icon_three_amount = models.IntegerField("数量", default=1)

    package = models.ForeignKey('package.Package')


    class Meta:
        db_table = 'checkin_item'
        unique_together = (
            ('checkin_date', 'index_number'),
        )
