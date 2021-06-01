import sys
import socket
import json
with open("input.json","r") as f:
    data=json.load(f)

fp = open("output.txt","w")


table=[[0 for i in range(len(data['network']))] for j in range(len(data['network']))]

for i in range(len(data['network'])):
    for j in data['network'][i][1]:
        table[i][j]=1

sys.stdout = fp

for i in range(len(data['input'])):
    for j in data['input'][i]:
        if(table[j[0]][j[1]] == 1): print("r%d"%j[1],":",j[2])
        else : print("r%d"%j[1],":",j,"Unreachable")