import datetime as dt
import requests
import json


#######################################################
###
### Input: none
### Function: Get the day ahead prices from Frank Energie (upcomming prices as far as possible into the future)
### Output: List upcomming prices in the format: list[time, price buy, price sell]
###
### https://devpress.csdn.net/python/62f509cfc6770329307fb193.html
###
#######################################################

def Ophalen():
    nu = dt.datetime.now(dt.timezone.utc)
    net = nu - dt.timedelta(hours = 2)
    urlvandaag = "https://mijn.easyenergy.com/nl/api/tariff/getapxtariffs?startTimestamp="+str(net.year)+"-"+str(net.month)+"-"+str(net.day)+"&endTimestamp=2100-01-01&grouping="
    #print (urlvandaag)
    responsev = requests.get(urlvandaag, verify=False)
    cv = json.loads(responsev.text)
    returnvalues = []
    for x in cv:
        datum = dt.datetime.fromisoformat(x['Timestamp'])
        #print (datum)
        if ((datum.timestamp() - nu.timestamp()) >= -3600):
            #print (x['TariffUsage'])
            returnvalues.append([datum, x['TariffUsage'], x['TariffReturn']])
    return returnvalues
