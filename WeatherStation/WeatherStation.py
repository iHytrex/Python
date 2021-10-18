import machine;
import dht;
import time;
import network;
import urequests;


print("Starting...")

d = dht.DHT11(machine.Pin(4)); 
r = machine.Pin(2, machine.Pin.OUT);

def Conect(ssid, password): # Network method
    station = network.WLAN(network.STA_IF);
    station.active(True);
    station.connect(ssid, password);
    for i in range(50):
        if (station.isconnected()):
            break;
        time.sleep(0.1);
    return station;

print("Conecting...");
station = Conect("XXXXX","XXXXXXXXX");
if (not station.isconnected()):
    print("Connection Failed")
else:
    print("Connected");
    while True:
        d.measure();
        print("\n - Temperature: {} \n - Humidity: {}\n\n".format(d.temperature(),d.humidity()))
        site = urequests.get("https://api.thingspeak.com/update?api_key=G0DDPYOX8J1LZYRV&field1={}&field2={}".format(d.temperature(),d.humidity()));
        if (d.temperature() > 31 or d.humidity() > 70): 
            r.value(1);  #ON
        else:
            r.value(0); #OFF
            station.disconnect();
        site.close();
        time.sleep(60);
