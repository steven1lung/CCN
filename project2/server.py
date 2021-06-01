from interest import INTEREST
import threading
import json
import socket
import csv
import queue

class Server(threading.Thread):

    #def __init__(self, routerID, network, data, lock, HOST='127.0.0.1'):
    def __init__(self, serverID, sizes, producer_contents, run_start_time,network,lock,HOST='127.0.0.1'):
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.PORT= 8000 + serverID
        self.id = serverID
        self.network = network
        self.data = producer_contents
        self.lock=lock
        self.num=0
        self.Interest=INTEREST()
        self.interest_queue=queue.Queue(maxsize=sizes)
        self.time=0

    def run(self):
        self.interest_process()
        self.data_process()
        self.accept()
        # self.data_process()
  

    
    def start_network(self,run_start_time,frequency,content_num,server_id,interests):
        # print(server_id,end="")
        # print(" send to ",end="")
        data=interests['r'+str(server_id)]
        # print(data[0]['interest_ID'])
        # for i in data:
        # interest_id=data[run_start_time]['interest_ID']
        # content_name=data[run_start_time]['content_name']

        send_to=self.network['r'+str(server_id)]
        
        self.time=run_start_time
        interest_tmp=self.Interest.generate_interest(server_id,run_start_time,frequency,content_num,server_id,interests)
   
        for i in send_to:    
            # print(str(i)+" ")
            # for j in interest_tmp:
                # print(type(j))
            send_data=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            send_data.connect((self.HOST,8000+i))
            send_data.sendall(bytes(json.dumps(interest_tmp),encoding='utf-8'))
        
        # for j in interests:
        #     send_data=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #     send_data.connect((self.HOST,8000+send_to))
        #     send_data.sendall((bytes(json.dumps(j),encoding='utf-8')))    
     


    def accept(self):
        print("in accept")
        csv_columns=['type',
                    'interest_ID',
                    'consumer_ID',
                    'route_ID',
                    'content_name',
                    'interest_hop',
                    'life_hop',
                    'run_start_time',
                    'path'
                    ]

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen(10)
        with open('input_data/peremiters.json') as file:
            data=file.read()
        parameters=json.loads(data)
        with open('input_data/interests.json') as file:
            data=file.read()
        interests=json.loads(data)
        while True:
     
            conn, addr = server.accept()
            packet = conn.recv(1024)
            packet = json.loads(packet)
            # string = 'r' + str(self.id) + ' : ' +packet+ '\n'
            string=packet
            
            if(string['type']=='interest'):
                
                string['interest_hop']+=1
                string['path']=string['path']+str(self.id)+'/'
                # output_file = open('output_data/output.csv','a')
                # output_file.write(string)
                if(int(string['route_ID'])==self.id):
                    string['time']=self.time
                    self.lock.acquire()
                    with open('output_data/output_interest.csv','a') as f:
                        for key in string.keys():
                            f.write('%s: %s '%(key,string[key]))
                        f.write('\n')
                    self.lock.release()
                  
                else:
                    string['time']=self.time
                    self.lock.acquire()
                    with open('output_data/output_interest.csv','a') as f:
                        for key in string.keys():
                            f.write('%s: %s '%(key,string[key]))
                        f.write('\n')
                    self.lock.release()
                    self.interest_queue.put(string)
                    self.interest_process()
            
            elif(string['type']=='data'):
                print("get data!")
          
        
    def interest_process(self):
        print("in interest_process")

    def data_process(self):
        print("in data")







    
    # def send_data(self):
    #     network_list = self.network[1][:]
    #     for i in self.data:
    #         if i[1] in network_list:
    #             send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #             send_data.connect((self.HOST, 8000 + i[1]))
    #             send_data.sendall(bytes(json.dumps(i), encoding='utf-8'))
    #         else:
    #             string = 'r' + str(self.id) + ' : ' + str(i) + "Unreachable\n"
    #             self.lock.acquire()
    #             output_file = open('output_data/output.txt','a')
    #             output_file.write(string)
    #             output_file.close()
    #             self.lock.release()