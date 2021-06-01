
class PIT():
    def __init__(self):
        self.pit_dict={}

    def Create_pit(self,route_ID):
        self.pit_dict={
            'content_name': [],
            'inface':[],
            'outface':[]
        }
        return self.pit_dict

    def Get_pit(self):
        return self.pit_dict

    def Get_put_entrt(self,content_name):
        return self.pit_dict[content_name]

