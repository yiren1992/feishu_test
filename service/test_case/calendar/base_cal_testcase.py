#!/usr/bin/env python
# -*- coding: utf-8 -*-
from service.api.calendar.calendar import Calendar


class BaseCalTestCase:
    def setup_class(self):
        self.cal = Calendar()

