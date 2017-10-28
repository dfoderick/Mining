#David Foderick, Skylake Software Inc.
import sys
import os
import time
import subprocess
import json
import paho.mqtt.client as mqtt

#configuration section for your miner
yourminerapiscript = "minerapi.py"
apisummarycommand = "summary"
apistatscommand = "stats"
yourmineripaddress = "127.0.0.1"
yourminerport = "4028"

#configuration section for Cayenne
username = "your cayenne user code goes here"
password = "your cayenne password code goes here"
clientid = "your cayenne clientid/deviceid goes here"

mqttc = mqtt.Client(client_id=clientid)
mqttc.username_pw_set(username, password=password)
mqttc.connect("mqtt.mydevices.com", port=1883, keepalive=120)
mqttc.loop_start()

topic_miner_hash = "v1/" + username + "/things/" + clientid + "/data/1"
topic_miner_temp1 = "v1/" + username + "/things/" + clientid + "/data/2"
topic_miner_temp2 = "v1/" + username + "/things/" + clientid + "/data/3"
topic_miner_temp3 = "v1/" + username + "/things/" + clientid + "/data/4"

while True:
    try:
	#call the cgminer api of our asic machine
	callminer = subprocess.Popen(["python",yourminerapiscript, apistatscommand, yourmineripaddress, yourminerport], stdout=subprocess.PIPE)
	apiresponse = callminer.stdout.read()
	#fudge the json return results, apparently a bug in cgminer stats result
	statsstart = apiresponse.find('}{"STATS"')+1
	statsend = apiresponse.find('}],"id":1}')+1
	juststats = apiresponse[statsstart:statsend]
	jsonstats = json.loads(juststats)
	#pull out the values we are interested in. In this case monitor the real time hash rate and temperature
	minercount = jsonstats['miner_count']
	currenthash = jsonstats['GHS 5s']
	tempboard1 = jsonstats['temp6']
	tempboard2 = jsonstats['temp7']
	tempboard3 = jsonstats['temp8']
	print str(currenthash)+' '+str(minercount)+' '+str(tempboard1)+' '+str(tempboard2)+' '+str(tempboard3)
	
	if currenthash is not None:
		hashvalue = "freq,hz=" + str(currenthash)
		mqttc.publish(topic_miner_hash, payload=hashvalue, retain=True)
	if tempboard1 is not None:
		temp1value = "temp,c=" + str(tempboard1)
		mqttc.publish(topic_miner_temp1, payload=temp1value, retain=True)
	if tempboard2 is not None:
		temp2value = "temp,c=" + str(tempboard2)
		mqttc.publish(topic_miner_temp2, payload=temp2value, retain=True)
	if tempboard3 is not None:
		temp3value = "temp,c=" + str(tempboard3)
		mqttc.publish(topic_miner_temp3, payload=temp3value, retain=True)
	time.sleep(60)
    except (EOFError, SystemExit, KeyboardInterrupt):
        mqttc.disconnect()
        sys.exit()
