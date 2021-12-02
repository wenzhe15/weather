import get_path as g
import valideer as V
import pandas as pd
import json
import os

with V.parsing(ignore_optional_property_errors=True, additional_properties=False):
    geojson_validator = V.parse({
        "+type": V.Enum(["FeatureCollection"]),
        "+features":[{
        "+type": V.Enum(["Feature"]),
        "geometry": {"+type": V.Enum(["Point", "LineString", "Polygon"]),
                        "coordinates":[["number"]]},
        "+properties": {"+name":V.Enum(["LLJ", "W_SNOW", "E_SNOW", "WET_SN", 
                                        "CUM_SN", "COLD_FRONT", "WARM_FRONT", 
                                        "OCC_FRONT", "H_POINT", "L_POINT", "HLJ", 
                                        "TYPOON", "R_START", "R_STOP", "RA_SN", "HAIL"])} 
                    }]              
        })

#json_validator = V.parse()

def check(data, validator):
    path = None
    bvalue = None
    bkind = None
    msg = None
    try:
        validator.validate(data)
                
    except Exception as e:
        print(str(e))
        #print("잘못 들어간 값" + str(e).split(' ')[2])
        if "additional properties" in str(e):
            bvalue = str(e).split(' ')[-3][1:-1]
            bkind = "additional properties"
            msg = str(e)
        else:
            bvalue = str(e).split(' ')[2]
            bkind = "enum"
            msg = str(e)
        print(f"! Error_path:"+ str(e).split(' ')[-1][:-1])
        path = str(e).split(' ')[-1][:-1]
    
    return path, bkind, bvalue, msg

        
def main():
    target = 'D:\\ssh\\project\\weather\\CODE\\test_jsondata'

    df = pd.DataFrame(columns=["파일명","오류 위치","검사 항목","오류 값", "오류 메세지"])
    for i, filepath in enumerate(g.get_json(target)):
        print("filepath:", filepath)
        with open(filepath, 'r') as f:
            json_data = json.load(f)
            filename = os.path.basename(filepath) # filepath.split('\\')[-1] #
            print("filename:", filename)
            path, bkind, bvalue, msg = check(json_data, geojson_validator)
            print("오류 위치:", path)
            print("오류 값", bvalue)
            print('------------')

            if path==None:
                continue

            df.loc[i] = [filename, path, bkind, bvalue, msg]
            print(df)
    
if __name__ == "__main__":
	main()