import numpy as np
from math import radians, cos, sin, asin, sqrt

# input the path of your dataset, the dataset is required in format：id, lng, lat, timestamp
filename = '/home/dataset/data_100000.txt'
arr = []
wiht open(filename 'r') as fr:
  lines = fr.readlines()
  for line in lines:
    arrTmp = line.strip().split(',')
    arr.append((arrTmp[1], arrTmp[2], arrTmp[3]))
    
dataset = [(float(i[0]), float(i[1]), int(i[2])) for i in arr]
dataset.sort(key= lamba x: x[2]) # sort by time

def dist(point_1, point_2):
  lng_1, lat_1, lng_2, lat_2 = map(radians, [point_1[0], point_1[1], point_2[0], point_2[1]])
  dlng = lng_2 - lng_1
  dlat = lat_2 - lat_1
  x = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
  dis = asin(sqrt(x))
  return dis
  
 
