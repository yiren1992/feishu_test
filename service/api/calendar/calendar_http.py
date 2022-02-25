#!/usr/bin/env python
# -*- coding: utf-8 -*-
from service.api.base_page import BasePage


class CalendarHttp(BasePage):
    base_url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
    user_id = '4f3d4ca6'

    def get_cal(self):
        url = self.base_url + '/primary'
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        r = self.send('POST', url, headers=header)
        print(r.json())
        return r.json()

    def create(self, summary: str, description: str, permissions: str, color: int, summary_alias: str):
        """
        permissions（日历公开范围）以下值三选一：
            private：私密
            show_only_free_busy：仅展示忙闲信息
            public：他人可查看日程详情
        """
        header = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            "summary": summary,
            "description": description,
            "permissions": permissions,
            "color": color,
            "summary_alias": summary_alias
        }
        r = self.send('POST', self.base_url, headers=header, json=data, verify=False)
        print(r.json())
        print(self.token)
        return r.json()

    def delete(self, calendar_id):
        url = self.base_url + f'/{calendar_id}'
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        r = self.send('DELETE', url, headers=header)
        return r.json()

    def get(self, calendar_id):
        url = self.base_url + f'/{calendar_id}'
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        r = self.send('GET', url, headers=header)
        print(r.json())
        return r.json()

    def get_list(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        r = self.send('GET', self.base_url, headers=header)
        print(r.json())
        return r.json()

    def update(self, calendar_id, summary: str, description: str, permissions: str, color: int, summary_alias: str):
        url = self.base_url + f'/{calendar_id}'
        header = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        body = {
            "summary": summary,
            "description": description,
            "permissions": permissions,
            "color": color,
            "summary_alias": summary_alias
        }
        r = self.send('PATCH', url, headers=header, json=body)
        print(r.json())
        return r.json()

    def search(self, query):
        url = self.base_url + '/search'
        header = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        body = {
            "query": query
        }
        r = self.send('POST', url, headers=header, json=body, verify=False)
        print(r.json())
        return r.json()

    def subscribe(self, calendar_id):
        url = self.base_url + f'/{calendar_id}/subscribe'
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        r = self.send('POST', url, headers=header)
        print(r.json())
        return r.json()

    def unsubscribe(self, calendar_id):
        url = self.base_url + f'/{calendar_id}/unsubscribe'
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        r = self.send('POST', url, headers=header)
        print(r.json())
        return r.json()


