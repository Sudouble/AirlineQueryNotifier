# coding: utf-8

import json
import requests
# from urllib.parse import quote
from urllib import pathname2url as quote
from collections import OrderedDict
from colorama import Fore
from prettytable import PrettyTable

class CtripAir():

    # 生成城市代码， id， 请求头， post参数
    def __init__(self, dcity, acity, date):
        dcity_code, dcity_id = self.get_city_code(dcity)
        acity_code, acity_id = self.get_city_code(acity)
        dcity = quote(dcity)
        acity = quote(acity)
        self.date = date
        # self.url = 'itinerary/api/12808/products'
        self.url = 'https://flights.ctrip.com/itinerary/api/12808/products'
        refer = 'http://flights.ctrip.com/p://flights.ctrip.com/itinerary/oneway/{dcity}-{acity}?date={date}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0(Windows NT10.0;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
            'Referer': refer,
            'Content-Type': 'application/json;charset=utf-8',
        }
        self.payload = {
            "flightWay":"Oneway",
            "classType":"ALL",
            "hasChild":False,
            "hasBaby":False,
            "searchIndex":1,
            "airportParams":[
                {"dcity": dcity_code,
                 "acity": acity_code,
                 # "dcityname": dcity,
                 # "acityname": acity,
                 "date": date,
                 "dcityid": dcity_id,
                 "acityid": acity_id
                 }
            ]}

    # 获取城市 code、 id
    def get_city_code(self, name):
        try:
            url = 'http://flights.ctrip.com/itinerary/api/13076/getpoicontent?key=%s' % name
            print url
            res = requests.get(url)
            city_code = res.json()['data']['Data'][0]['Code']
            city_id = res.json()['data']['Data'][0]['CityId']
            return city_code, city_id
        except Exception as e:
            print('城市名称错误{e}')

    # 发起post请求，返回json数据
    def start_request(self):
        try:
            res = requests.post(url=self.url, headers=self.headers, data=json.dumps(self.payload))
            if res.status_code == 200:
                route_list = res.json()['data']['routeList']
                return route_list
                print('网页信息貌似不对哦')
        except Exception as e:
            print(e), ' Error'

    # 解析机票信息
    def parse(self, route_list):
        try:
            tickets = []
            for route in route_list:
                ticket = OrderedDict()
                try:
                    flane = route['legs'][0]
                    flight = flane['flight']
                    ticket['air_no'] = flight['flightNumber']
                    ticket['date'] = self.date
                    ticket['company'] = flight['airlineName']
                    # ticket['craft_type'] = flight['craftTypeName']

                    depart_info = flight['departureAirportInfo']
                    # ticket['depart_city'] = depart_info['cityName']
                    depart_airport = depart_info['airportName']
                    depart_gateway = depart_info['terminal']['name']
                    ticket['depart'] = depart_airport+''+depart_gateway
                    depart_time = flight['departureDate']
                    ticket['depart_time'] = depart_time

                    arrival_info = flight['arrivalAirportInfo']
                    # ticket['arrival_city'] = arrival_info['cityName']
                    arrival_airport = arrival_info['airportName']
                    arrival_gateway = arrival_info['terminal']['name']
                    ticket['arrival'] = arrival_airport + ' '+ arrival_gateway
                    ticket['arrival_time'] = flight['arrivalDate']

                    lowest_price = flane['characteristic']['lowestPrice']
                    ticket['lowest_price'] = lowest_price
                    # ticket['standardprices'] = flane['characteristic']['standardPrices']
                    # print(ticket)
                except KeyError:
                    lowest_price = None
                    pass
                if lowest_price:
                    tickets.append(ticket)
            return tickets
        except TypeError:
            pass

    def __call__(self):
        res = self.start_request()
        tickets = self.parse(res)
        return tickets

def pretty_air(tickets):
    header = '航班型号 起飞日期 航空公司 起飞机场 起飞时间 降落机场 降落时间 最低价格'.split()
    pt = PrettyTable()
    pt._set_field_names(header)
    try:
        for ticket in tickets:
            pt.add_row(ticket.values())
        print(pt)
        return pt
    except TypeError:
        pass

if __name__ == '__main__':
    dcity = '北京'
    acity = '青岛'
    date = '2019-05-01'
    air_tickets = CtripAir(dcity, acity, date)()
    pretty_air(air_tickets)

