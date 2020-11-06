import urllib.request
import pandas as pd
import ast

contents = urllib.request.urlopen("https://apps.bea.gov/api/data/?&UserID=147C3513-87FA-47A4-94F4-7249219008E9&method=GetData&datasetname=Regional&TableName=SQINC1&GeoFIPS=STATE&LineCode=1&ResultFormat=CSV").read()

decoded_content = ast.literal_eval(contents.decode('utf-8'))

def create_dict_recursively(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from create_dict_recursively(value)
        else:
            yield (key, value)

for key, value in create_dict_recursively(decoded_content):
    if key == 'Data':
        data = value
        
df = pd.DataFrame(data)

df.to_csv('PersonalIncome.csv', index = False) 
