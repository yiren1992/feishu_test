#!/usr/bin/env python
# -*- coding: utf-8 -*-
from service.api.base_page import BasePage
from service.api.calendar.calendar_http import CalendarHttp


class Calendar(BasePage):
    """
    日历管理
    calendar api的统一设置
    业务与实现分离
    """

    # 获取主日历
    def get_cal(self):
        return CalendarHttp().get_cal()

    # 创建日历
    def create(self, summary, description, permissions, color, summary_alias):
        return CalendarHttp().create(summary, description, permissions, color, summary_alias)

    # 删除日历
    def delete(self, calendar_id):
        return CalendarHttp().delete(calendar_id)

    # 获取日历
    def get(self, calendar_id):
        return CalendarHttp().get(calendar_id)

    # 获取日历列表
    def get_list(self):
        return CalendarHttp().get_list()

    # 更新日历
    def update(self, calendar_id, summary, description, permissions, color, summary_alias):
        return CalendarHttp().update(calendar_id, summary, description, permissions, color, summary_alias)

    # 搜索日历
    def search(self, query):
        return CalendarHttp().search(query)

    # 订阅日历
    def subscribe(self, calendar_id):
        return CalendarHttp().subscribe(calendar_id)

    # 取消订阅日历
    def unsubscribe(self, calendar_id):
        return CalendarHttp().unsubscribe(calendar_id)


class TestGet:
    def test_get(self):
        r = Calendar().search('测试')
        assert r['code'] == 0

    def test_create(self):
        Calendar().create('测试12m34', '123456', 'private', -1, '198')

    def test_1(self):
        Calendar().unsubscribe('feishu.cn_ig7XkyASvsWJSD2RllLZKe@group.calendar.feishu.cn')

