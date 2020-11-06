import requests
import os
import json
import prettytable
headers = {'Content-type': 'application/json'}


StartYear=input("Enter Trends Start Date: (Ex: 2016) ")
EndYear=input("Enter Trends End Date: (Ex: 2018) ")

data = json.dumps({"seriesid": ['CUUR0000SA0'],"startyear":StartYear, "endyear":EndYear})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']

        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
        if 'M01' <= period <= 'M12':
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(seriesId + '.csv','w')
    output.write (x.get_string())
    output.close()
    os.system("sh mvfile.sh")
    os.system("sh sh_execute_copy_to_s3.sh")
