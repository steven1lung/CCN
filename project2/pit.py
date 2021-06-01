

class PIT():
    def __init__(self):

    # Each router creates an independent PIT table
    def Creat_pit(self, route_ID):

    def Get_pit(self):

    # Get the entry of the content name from the pit
    def Get_pit_entry(self, content_name):

    # The outface is updated to pit
    def Update_pit_outface(self, pit, Outfaces, interest):

    # The inface of the received interest packet is merged into the same content name
    def Merge_pit_entry(self, interest):
        
    # Create a pit entry
    def Create_pit_entry(self, interest):
    
    # Check whether there is an entry matching the content name od the interest packet in the pit
    def Search_pit_data(self, pit, data):

    # The content_name entry is removed from pit
    def Remove_pit_entry(self, pit, data):
