from router import Router
import json
import threading

def main():
    router_list = []
    # read network
    with open('network.json', 'r') as file:
        data = file.read()
    network = json.loads(data)
    # print("finish read data")

    # read producer_contents
    with open('producer_contents.json') as file:
        data=file.read()
    producer_contents=json.loads(data)
    # print(producer_contents['r0'])


    #network = parse['network']
    #data_list = parse['input']
    #lock = threading.Lock()

    # print("finish parse")

    # run network
    #for i in range(len(network)):
    #    router = Router(i, network[i], data_list[i], lock)
    #    router.start()
    #    router_list.append(router)
    # print("finish i")
    #for j in router_list:
    #    j.send_data()
    # print("finish j")

if __name__ == '__main__':
    main()