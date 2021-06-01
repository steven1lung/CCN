
import json

class INTEREST():
    def __init__(self):
        self.interest = []

    # Consumer generated interest packet
    def Generate_interest(self, route_ID, run_start_time, frequency, content_num, route_num, interest):


    #  Check whether the interest packet has timed out
    def Time_out(self, interest):


    # Pack the interest packet to be sent and the output interface
    def Send_interest(self, pit, Outfaces, route_ID, interest):


    # Interest packet processing
    def On_interest(self, route_ID, interest, tables):


    # output information of the interest packet
    def Output_interest_txt(self, interest, times, result, hit, miss):


    def Drop_interest(self, route_ID, interest):
        