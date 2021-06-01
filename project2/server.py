import threading
import json
import socket

class Server(threading.Thread):

    #def __init__(self, routerID, network, data, lock, HOST='127.0.0.1'):
    def __init__(self, serverID, sizes, producer_contents, run_start_time,network, HOST='127.0.0.1'):
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.PORT= 8000 + serverID
        self.id = serverID
        self.network = network
        self.data = producer_contents


    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen(10)

        while True:
            conn, addr = server.accept()
            packet = conn.recv(1024)
            packet = json.loads(packet)
            string = 'r' + str(self.id) + ' : ' + packet[2] + '\n'
            self.lock.acquire()
            output_file = open('output_data/output.txt','a')
            output_file.write(string)
            output_file.close()
            self.lock.release()
    
    # def start_network(self,run_start_time,frequency,content_num,route_num,interests):
    #     while True:
    #         #asdsad

    # def accept(self):
    #     #asdasd
    # def interest_process(self):
    #     #asdasd
    # def data_process(self):
    #     #asdasd







    
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