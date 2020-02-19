import pyshark
from os import path, sys, walk
from time import sleep
cnt = 0
paths_pcap = []
for f in walk(sys.path[0]):
    cnt += 1
    folder_name = f[0]
    for iterable in f:
        if type(iterable) is list:
            for item in iterable:
                if item.split(".")[-1] == 'pcap':
                    file_path = folder_name + "/"+ item
                    paths_pcap.append(file_path)
                    
def convert_pcap(pcap_path):
    r = pyshark.FileCapture(pcap_path, only_summaries=True)
    res = []
    # try:
    for l in r:
        sleep(0.0001)
    res.append(str(l))
    # except RuntimeError:
    #     res = []
    #     for l in r:
    #         res.append(str(l))
    print(len(res))

for p_path in paths_pcap:
    convert_pcap(p_path)
    sleep(1)