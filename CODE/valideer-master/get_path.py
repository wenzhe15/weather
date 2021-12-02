import os
import numpy as np
import pandas as pd

#target = 'C:\workspace\data' # recursive search 를 시작할 디렉토리 위치

def get_geojson(target):
    geojson_full_path = []
    for root, dirnames, files in os.walk(target): # search를 시작하는 위치부터 모든 디렉토리를 돌면서 
        for x in files:
            if x.endswith('.geojson'):            # 확장자가 geojson 파일만 조건으로 찾아옵니다.
                full_path = root +'\\' + x
                geojson_full_path.append(full_path) # 전체경로를 geojson_full_path 에 담아서 반환합니다.
    return geojson_full_path


def get_json(target):
    geojson_full_path = []
    for root, dirnames, files in os.walk(target): # search를 시작하는 위치부터 모든 디렉토리를 돌면서 
        for x in files:
            if x.endswith('.json'):            # 확장자가 geojson 파일만 조건으로 찾아옵니다.
                full_path = root +'\\' + x
                geojson_full_path.append(full_path) # 전체경로를 geojson_full_path 에 담아서 반환합니다.
    return geojson_full_path
# print(get_json(target))