# coding: utf-8

from QueryFeizhu import QueryFeizhu
from QueryCtrip import CtripAir
from TickFilter import TickFilter
from prettytable import PrettyTable
from EmailSender import EmailSender

receiver = ["xxx@163.com"]

def pretty_air(tickets):
    header = '航班型号 起飞日期 航空公司 起飞机场 起飞时间 降落机场 降落时间 最低价格'.split()
    pt = PrettyTable()
    pt._set_field_names(header)
    try:
        for ticket in tickets:
            pt.add_row(ticket.values())
        return pt
    except TypeError:
        pass

if __name__ == '__main__':
    dcity = '北京'
    acity = '杭州'
    date = '2019-10-02'

    last_message = ''

    air_tickets = CtripAir(dcity, acity, date)()
    # print pretty_air(air_tickets)
    #
    # filtered = TickFilter(air_tickets, 900).filter()
    #
    # if filtered != last_message:
    #     email_sender = EmailSender(receiver)
    #
    #     msg = pretty_air(filtered)
    #     email_sender.send_email(msg.get_string())
    #
    # last_message = filtered

# if __name__ == '__main__':
#     dep_city = "北京"
#     arr_city = "杭州"
#     time = '2019-05-02'
#     query_feizhu = QueryFeizhu(dep_city, arr_city, time)
#     for each in query_feizhu.Query():
#         print each

