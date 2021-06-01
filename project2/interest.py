import json

class INTEREST():
    def __init__(self):
        self.interest={}
        self.count=0

    def generate_interest(self,routerID,run_start_time,frequency,content_num,route_num,interests):
        data=interests['r'+str(routerID)]
        send=int(data[run_start_time]['content_name'][1])
        if(not data[run_start_time]['content_name'][2] == '/'):
            send=send+int(data[run_start_time]['content_name'][2])
        send=str(send)
        self.interest={
            'time':0,
            'type':'interest',
            'interest_ID': data[run_start_time]['interest_ID'],
            'consumer_ID':routerID,
            'route_ID': send,
            'content_name':data[run_start_time]['content_name'],
            'interest_hop':0,
            'life_hop':5,
            'run_start_time':run_start_time,
            'path':str(routerID)+'/'
        }
        self.count+=1
        return self.interest