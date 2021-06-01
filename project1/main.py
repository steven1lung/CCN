from router import Router
import json
import threading

def main():
    router_list = []
    # read file
    with open('input_data/input.json', 'r') as file:
        data = file.read()

    # parse file
    parse = json.loads(data)
    network = parse['network']
    data_list = parse['input']
    lock = threading.Lock()

    # run network
    for i in range(len(network)):
        router = Router(i, network[i], data_list[i], lock)
        router.start()
        router_list.append(router)

    for j in router_list:
        j.send_data()

if __name__ == '__main__':
    main()