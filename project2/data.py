

class DATA():
    def __init__(self):

    # Create a data packet
    def Create_data(self, route_ID, interest):
    
    # Pack the data packet to be sent and the output interface
    def Send_data(self, Infaces, roure_ID, data):
    
    # data packet processing
    def On_data(self, sizes, route_ID, data, tables):

    def Drop_data(self, inface, data):

    # output information of the data packet
    def Output_data_txt(self, data, times, result, hit_consumer, hit_PIT, miss_PIT):
        