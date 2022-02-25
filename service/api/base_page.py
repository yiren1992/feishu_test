#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


class BasePage:
    """
    飞书的api公共特性，获取token，获取身份信息，解决跟业务稍微沾边的所有api的通用特性
    解决最底层的请求的发送问题，封装requests等库的细节，实现与具体的请求工具无关
    """
    def __init__(self):
        self.session = requests.Session()
        self.token = self.get_token()
        # self.session.params = {'access_token': self.token}

    def get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        header = {
            "Content-Type": "application/json; charset=utf-8"
        }
        body = {
            "app_id": "cli_a281cec836f89013",
            "app_secret": "kK6Sw864y2U7fo7nKylXNhvpvIWQYkqn"
        }
        r = self.session.post(url, headers=header, params=body, verify=False)
        return r.json()['tenant_access_token']

    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)
