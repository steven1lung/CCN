import json

class NETWORK():
    def __init__(self):
        self.network=[]

    def Create_network(self,network):
        self.network=network
        return self.network

    def Get_network(self):
        return self.network