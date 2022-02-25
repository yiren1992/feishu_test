#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
import sys

sys.path.append('/Users/wanghuifang/Desktop/py/GitHub/feishu_test')

from service.test_case.calendar.base_cal_testcase import BaseCalTestCase
from service.utils import Utils


@allure.feature('日历接口测试')
class TestCalendar(BaseCalTestCase):

    @allure.story('获取主日历')
    @allure.title('获取主日历')
    def test_get_cal(self):
        r = self.cal.get_cal()
        assert r['code'] == 0
        print(sys.path)

    @allure.story('创建日历')
    @allure.title('创建日历，测试数据：{dic}')
    @pytest.mark.parametrize('dic', Utils.load_yaml('/Users/wanghuifang/Desktop/py/GitHub'
                                                    '/feishu_test/service/data/calendar.yml', 'create'))
    def test_create(self, dic):
        r = self.cal.create(dic['summary'], dic['description'], dic['permissions'], dic['color'], dic['summary_alias'])
        assert r['code'] == 0
        assert r['msg'] == 'success'

    @allure.story('删除日历')
    @allure.title('删除日历:{calendar_id}')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('calendar_id', ['feishu.cn_Vsp3BaFn0DKPadbH2mNp2f@group.calendar.feishu.cn'])
    def test_delete(self, calendar_id):
        r = self.cal.delete(calendar_id)
        assert r['code'] == 0, r['msg'] == 'success'

    @allure.story('获取日历')
    @allure.title('获取日历:{calendar_id}')
    @pytest.mark.parametrize('calendar_id', ['feishu.cn_nCBZbyS9c8JP1VFziJD7Df@group.calendar.feishu.cn'])
    def test_get(self, calendar_id):
        r = self.cal.get(calendar_id)
        assert r['code'] == 0, r['calendar_id'] == calendar_id

    @allure.story('获取日历列表')
    @allure.title('获取日历列表')
    def test_get_list(self):
        r = self.cal.get_list()
        assert r['code'] == 0

    @allure.story('更新日历')
    @allure.title('更新日历:{dic}')
    @pytest.mark.parametrize('dic', Utils.load_yaml('/Users/wanghuifang/Desktop/py/GitHub'
                                                    '/feishu_test/service/data/calendar.yml', 'update'))
    def test_update(self, dic):
        r = self.cal.update(dic['calendar_id'], dic['summary'], dic['description'], dic['permissions'], dic['color'],
                            dic['summary_alias'])
        assert r['code'] == 0, r['summary'] == dic['summary']

    @allure.story('搜索日历')
    @allure.title('搜索日历:{query}')
    @pytest.mark.parametrize('query', Utils.load_yaml('/Users/wanghuifang/Desktop/py/GitHub'
                                                      '/feishu_test/service/data/calendar.yml', 'search'))
    def test_search(self, query):
        r = self.cal.search(query)
        assert r['code'] == 0

    @allure.story('订阅日历')
    @allure.title('订阅日历: {calendar_id}')
    @pytest.mark.parametrize('calendar_id', ['feishu.cn_nCBZbyS9c8JP1VFziJD7Df@group.calendar.feishu.cn'])
    def test_subscribe(self, calendar_id):
        r = self.cal.subscribe(calendar_id)
        assert r['code'] == 0

    @allure.story('取消订阅日历')
    @allure.title('取消订阅日历: {calendar_id}')
    @pytest.mark.parametrize('calendar_id', ['feishu.cn_nCBZbyS9c8JP1VFziJD7Df@group.calendar.feishu.cn'])
    def test_unsubscribe(self, calendar_id):
        r = self.cal.unsubscribe(calendar_id)
        assert r['code'] == 0
