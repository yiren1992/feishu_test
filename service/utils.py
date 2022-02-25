#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


class Utils:
    @classmethod
    def load_yaml(cls, path, data_name):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        steps = data[data_name]
        return steps



