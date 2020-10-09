import http.client
import urllib
import time

key = "7481QW0APO2BO2BU"  
def thermometer():
    while True:
        
        K = "L1-F-5,b,yunzhouliu@cmail.carleton.ca"
        params = urllib.parse.urlencode({'field1': K, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (K)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        while True:
                thermometer()
 
