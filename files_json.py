__author__ = 'popov.sn'

import json


with open("C:/python_barancev_w/new_training_prsft/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)
