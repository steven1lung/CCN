from server import Server
from network import NETWORK
import json
import threading

def load_network():
    with open('input_data/network.json', 'r') as file:
        data = file.read()
    return json.loads(data)

def load_parameters():
    with open('input_data/peremiters.json') as file:
        data=file.read()
    return json.loads(data)

def input_producer_contents():
    with open('input_data/producer_contents.json') as file:
        data=file.read()
    return json.loads(data)

def input_interests():
    with open('input_data/interests.json') as file:
        data=file.read()
    return json.loads(data)

def main():
    server_list = []
    
    network = load_network() # read network
    producer_contents= input_producer_contents() # read producer_contents
    interests= input_interests() #read interests
    parameters=load_parameters() #read parameters
    lock=threading.Lock()
    
    #serverID, sizes, producer_contents, run_start_time,network, HOST='127.0.0.1'
    
    for i in range(len(network)):
        server=Server(i,parameters['queue_size'] ,producer_contents ,0,network,lock)
        server_list.append(server)
        server.start()

  

    time=0
    while True:
        if(time>=parameters['run_time']) :
            break
        # print("heello")
        # code here
        if(time%parameters['frequency']==0):
            for j in server_list:
                j.start_network(time,parameters['frequency'],parameters['content_num'],j.id,interests)
            
        time+=1



    #data_list = parse['input']
    # lock = threading.Lock()
    # run network
    # for i in range(len(network)):
    #     router = Router(i, network[i], data_list[i], lock)
    #     router.start()
    #     router_list.append(router)
    # for j in router_list:
    #     j.send_data()


if __name__ == '__main__':
    main()