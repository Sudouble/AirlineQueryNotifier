# coding: utf-8

import datetime
import json
import requests

class QueryFeizhu():
    def __init__(self, dep_city, arr_city, expect_time):
        self.url = 'https://sjipiao.fliggy.com/searchow/search.htm'
        self.dep_city = dep_city
        self.arr_city = arr_city
        self.expect_time = expect_time

    def Query(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        payload = {'depCityName': self.dep_city, 'arrCityName': self.arr_city, 'depDate': self.expect_time, '_input_charset': 'utf-8'}
        message = requests.get(self.url, params=payload, headers=headers).text
        print message
        message = message.strip()
        message = message[1:-2]  # 去掉首尾括号
        message_json = json.load(message)
        if message_json.get('data'):
            jsons = message_json.get('data')
            name = jsons.get('aircodeNameMap')           # 字典，保存航空公司缩写与中文名
            airport = jsons.get('airportMap')            # 字典，保存机场的缩写和中文名
            # print(name)
            # print(airport)
            flights = jsons.get('flight')
            for flight in flights:                       # 生成器
                yield {
                    '来自':'飞猪旅行',
                    '航班':name[flight.get('airlineCode')]+flight.get('flightNo'),          # 航空公司及航班
                    '出发机场':airport[flight.get('depAirport')],                           # 出发机场
                    '到达机场':airport[flight.get('arrAirport')],                           # 到达机场
                    '出发时间':flight.get('depTime'),                                       # 出发时间
                    '到达时间':flight.get('arrTime'),                                       # 到达时间
                    '最低票价(不含机建燃油费)':int(flight.get('cabin').get('price'))         # 最低票价
                }

    def sort_flight(self):
        pass

