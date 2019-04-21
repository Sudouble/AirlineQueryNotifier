# coding: utf-8

from QueryFeizhu import QueryFeizhu
from QueryCtrip import CtripAir
from TickFilter import TickFilter
from prettytable import PrettyTable

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
    acity = '上海'
    date = '2019-05-01'
    air_tickets = CtripAir(dcity, acity, date)()
    # pretty_air(air_tickets)

    filtered = TickFilter(air_tickets, 800).filter()
    pretty_air(filtered)

# if __name__ == '__main__':
#     dep_city = "北京"
#     arr_city = "杭州"
#     time = '2019-05-02'
#     query_feizhu = QueryFeizhu(dep_city, arr_city, time)
#     for each in query_feizhu.Query():
#         print each

