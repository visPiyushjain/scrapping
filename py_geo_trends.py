import pandas as pd
import datetime
import time
import s3fs
import boto3
import os
import glob
import sys
#import pathlib
from pytrends.request import TrendReq
#from botocore.exceptions import NoCredentialsError
pytrends = TrendReq(hl='en-US', tz=360)

os.system("sh sh_mv_google_trends_files_to_archive.sh")
def Convert(string):
        li=list(string.split(","))
        return li

def convert_space(string):
        li=string.split(" ")
        return li

kw=input("Enter the keyword ")
kw_list=Convert(kw)

#geo_name=input("Enter geo name (for country: use country code e.g. US For States: use CountryCode-Region Code e.g. US-NY) ")

g=["US-TX-662"
,"US-GA-525"
,"US-NY-532"
,"US-NM-790"
,"US-LA-644"
,"US-MI-583"
,"US-NM-634"
,"US-OK-634"
,"US-TX-634"
,"US-AK-743"
,"US-GA-524"
,"US-GA-520"
,"US-TX-635"
,"US-CA-800"
,"US-MD-512"
,"US-ME-537"
,"US-LA-716"
,"US-TX-692"
,"US-OR-821"
,"US-MT-756"
,"US-MS-746"
,"US-NY-502"
,"US-AL-630"
,"US-VA-559"
,"US-ID-757"
,"US-MA-506"
,"US-KY-736"
,"US-NY-514"
,"US-NH-523"
,"US-MT-754"
,"US-WY-767"
,"US-IA-637"
,"US-IL-648"
,"US-SC-519"
,"US-KY-564"
,"US-NC-517"
,"US-VA-584"
,"US-GA-575"
,"US-NE-759"
,"US-IL-602"
,"US-CA-868"
,"US-OH-515"
,"US-WV-598"
,"US-OH-510"
,"US-CO-752"
,"US-SC-546"
,"US-MO-604"
,"US-AL-522"
,"US-OH-535"
,"US-MS-673"
,"US-TX-600"
,"US-TX-623"
,"US-IL-682"
,"US-OH-542"
,"US-CO-751"
,"US-IA-679"
,"US-MI-505"
,"US-AL-606"
,"US-MN-676"
,"US-NM-765"
,"US-NY-565"
,"US-PA-516"
,"US-OR-801"
,"US-CA-802"
,"US-IL-649"
,"US-AK-745"
,"US-MN-724"
,"US-MI-513"
,"US-NC-570"
,"US-CA-866"
,"US-FL-571"
,"US-AR-670"
,"US-IN-509"
,"US-FL-592"
,"US-MT-798"
,"US-CO-773"
,"US-MI-563"
,"US-MT-755"
,"US-WI-658"
,"US-NC-518"
,"US-NC-545"
,"US-NC-567"
,"US-MS-647"
,"US-TX-636"
,"US-PA-566"
,"US-VA-569"
,"US-CT-533"
,"US-MS-710"
,"US-MT-766"
,"US-HI-744"
,"US-TX-618"
,"US-AL-691"
,"US-ID-758"
,"US-IN-527"
,"US-MS-718"
,"US-TN-639"
,"US-FL-561"
,"US-PA-574"
,"US-AR-734"
,"US-KS-603"
,"US-AK-747"
,"US-KS-616"
,"US-KY-557"
,"US-MN-702"
,"US-IN-582"
,"US-LA-642"
,"US-LA-643"
,"US-MI-551"
,"US-TX-749"
,"US-NV-839"
,"US-KY-541"
,"US-OH-558"
,"US-NE-722"
,"US-AR-693"
,"US-CA-803"
,"US-IN-529"
,"US-TX-651"
,"US-GA-503"
,"US-WI-669"
,"US-MN-737"
,"US-MI-553"
,"US-OR-813"
,"US-TN-640"
,"US-AL-711"
,"US-FL-528"
,"US-WI-617"
,"US-MN-613"
,"US-MT-687"
,"US-MT-762"
,"US-AL-686"
,"US-AR-628"
,"US-CA-828"
,"US-AL-698"
,"US-TN-659"
,"US-LA-622"
,"US-NJ-501"
,"US-NC-544"
,"US-NE-740"
,"US-TX-633"
,"US-OK-650"
,"US-IA-652"
,"US-FL-534"
,"US-MO-631"
,"US-IL-632"
,"US-CA-804"
,"US-FL-656"
,"US-WV-597"
,"US-IL-675"
,"US-PA-504"
,"US-AZ-753"
,"US-PA-508"
,"US-OR-820"
,"US-ME-500"
,"US-ME-552"
,"US-MA-521"
,"US-IL-717"
,"US-NC-560"
,"US-SD-764"
,"US-CA-811"
,"US-VA-556"
,"US-VA-573"
,"US-IA-611"
,"US-NY-538"
,"US-IL-610"
,"US-CA-862"
,"US-DE-576"
,"US-NV-770"
,"US-TX-661"
,"US-TX-641"
,"US-CA-825"
,"US-CA-807"
,"US-CA-855"
,"US-GA-507"
,"US-WA-819"
,"US-OK-657"
,"US-AR-612"
,"US-IA-624"
,"US-NE-725"
,"US-IN-588"
,"US-ID-881"
,"US-AR-619"
,"US-MA-543"
,"US-KS-638"
,"US-IL-609"
,"US-NY-555"
,"US-FL-530"
,"US-FL-539"
,"US-IL-581"
,"US-OH-547"
,"US-KS-605"
,"US-MI-540"
,"US-TN-531"
,"US-AZ-789"
,"US-OK-671"
,"US-ID-760"
,"US-TX-709"
,"US-NY-526"
,"US-TX-626"
,"US-TX-625"
,"US-MD-511"
,"US-NY-549"
,"US-WI-705"
,"US-FL-548"
,"US-OH-554"
,"US-OK-627"
,"US-KS-678"
,"US-PA-577"
,"US-NC-550"
,"US-OR-810"
,"US-OH-536"
,"US-AZ-771"
,"US-OH-596"]

TF_Date=input("Enter Trends Start Date: (Ex: 2016-01-31) ")
TF_Date1=input("Enter Trends End Date: (Ex: 2018-01-31) ")
final_date = TF_Date + ' ' + TF_Date1

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

fileinterestovertime=glob.glob('InterestOverTime/*')
for f in fileinterestovertime:
    os.remove(f)


for geo_name in g:
    pytrends.build_payload(kw_list, cat=0, timeframe=final_date, geo=geo_name, gprop='')
    print(pytrends.interest_over_time())
    df_interest_time=pytrends.interest_over_time()
#    df_interest_time.to_csv('InterestOverTime_'+str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv')
    df_interest_time.to_csv(os.path.join('InterestOverTime',geo_name+'Interestovertime_'+listToString(kw_list[0])+'_'+str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'))
   # time.sleep(20)
 #   df.to_csv(os.path.join('RegionNames','Region_'+listToString(df2[ind])+'_'+listToString(kw_list[0])+'_'+str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'))

    #uploaded = upload_to_aws(df_interest_time.to_csv('InterestOverTime.csv'), 'nomis-one', 'test/test3')




#data_Region=[]
data_Interest_OverTime=[]


for name in glob.glob('InterestOverTime/*'):
    frameinterest=pd.read_csv(name)
    frameinterest['filename']=os.path.basename(name)
    print(frameinterest)
    data_Interest_OverTime.append(frameinterest)

bigframeIOT=pd.concat(data_Interest_OverTime,ignore_index=True)
bigframeIOT.to_csv('InterestOverTimeAWS/InterestOverTime'+listToString(kw_list[0])+'_'+str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv')





os.system("sh sh_execute_s3_google_trends.sh")
