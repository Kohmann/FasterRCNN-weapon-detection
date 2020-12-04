import numpy as np
import pandas as pd
import os

def get_box_and_names(index):
    i = index
    boxes = list()
    labels = list()
    
    boxes.append([data.iloc[i,4], data.iloc[i,5], data.iloc[i,6], data.iloc[i,7]])
    labels.append(data.iloc[i,3])
    while (data.iloc[i,0] == data.iloc[i+1,0]):
        boxes.append([data.iloc[i+1,4], data.iloc[i+1,5], data.iloc[i+1,6], data.iloc[i+1,7]])
        labels.append(data.iloc[i+1,3])
        i+=1
        if len(data.index)-1 == i:
            break
    return [boxes,labels]

def baggage_csv_reader(path_to_csv_dir):
    dic = {}
    for file in os.listdir(path_to_csv_dir):
        data = pd.read_csv(path_to_csv_dir+"/"+file)
        for i in range(len(data.index)):
            if (i<(len(data.index)-1)):
                dic[data.iloc[i,0][-14:]] = get_box_and_names(i)
                
    return dic