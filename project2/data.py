import json
import csv


class DATA():

    def __init__(self):

        self.data_dictionary={}
        


    def Create_data(self, route_ID, interest):
        self.data_dictionary = {

            'type': 'data',
            'consumer_ID': 0000,
            'route_ID': 0,
            'content_name': 'r0/00',
            'content_data': 'r0/000',
            'data_hop': 0,
            'run_start_time': 0,
            'path': 'p0/'

        }
    def send_data(self, Infaces, route_ID, data):
        self.data_dictionary[data_hop]+=1
        route_ID = route_ID + self.data_dictionary[path]

    def On_data(self, sizes, route_ID, data, tables):
        con_name = self.data_dictionary[content_name]
        if( con_name == )
            if( route_ID == tables[])
                #data hit in consumer
                Output_data_txt(self, tables[data],tables[times],"data hit in consumer",1,0,0)
            else
                #data hit in pit
                Output_data_txt(self, tables[data],tables[times],"data hit in pit",0,1,0)
                Forward
        else
            #data miss in pit
    
    def Drop_data(self, inface, data):
        #'Data miss in PIT
        self.data_dictionary={}

    def Output_data_txt(self, data, times, result, hit_cunsumer, hit_PIT, miss_PIT):
        with open('output_data/output_data.csv','a') as f:
                for key in string.keys():
                    f.write('%s: %s '%(key,string[key]))
                f.write('\n')