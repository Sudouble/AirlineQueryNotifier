# coding:utf-8

import datetime

class TickFilter():
    def __init__(self, tickets, exp_price, exp_fly_time=None):
        self.tickets = tickets
        self.exp_price = exp_price
        self.exp_fly_time = exp_fly_time

    def filter(self):
        result_ticket = []
        for ticket in self.tickets:
            depart_time = ticket['depart_time']
            depart_datetime = datetime.datetime.strptime(depart_time, '%Y-%m-%d %H:%M:%S')
            # ticket['arrival_time']
            # ticket['date']
            current_price = ticket['lowest_price']
            if self.exp_fly_time is not None and depart_datetime < self.exp_fly_time:
                continue
            if current_price <= self.exp_price:
                result_ticket.append(ticket)
        return result_ticket

