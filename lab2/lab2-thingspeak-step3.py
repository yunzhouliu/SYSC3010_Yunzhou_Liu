import httplib
import urllib
import time

def read():
    NEW_URL = "https://api.thingspeak.com/channels/1156691/feeds.json?api_key=PRVIVMMKK6KAE88A&results=2"
    get_data = requests.get(NEW_URL).json()
    channel_id=get_data["channel"]["id"]

    feild_1 = get_data["feeds"]
    
    t =  []
    for x in feild_1:
        t.append(x["field1"])

if __name__=="__main__":
    read()
