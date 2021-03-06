import threading
import json
import socket

class Router(threading.Thread):

    def __init__(self, routerID, network, data, lock, HOST='127.0.0.1'):
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.PORT= 8000 + routerID
        self.id = routerID
        self.network = network
        self.data = data
        self.lock = lock

    def run(self):
        print('in run')
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

    def send_data(self):
        network_list = self.network[1][:]
        for i in self.data:
            if i[1] in network_list:
                send_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                send_data.connect((self.HOST, 8000 + i[1]))
                send_data.sendall(bytes(json.dumps(i), encoding='utf-8'))
            else:
                string = 'r' + str(self.id) + ' : ' + str(i) + "Unreachable\n"
                self.lock.acquire()
                output_file = open('output_data/output.txt','a')
                output_file.write(string)
                output_file.close()
                self.lock.release()
