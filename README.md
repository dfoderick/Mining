# Mining
Scripts for bitcoin mining

Use uploadhash.py to upload hash rate and miner temps to mydevices.com Cayenne dashboard.
This will make the miner stats available on mobile device or web interface where you can get alerts when your miner is in trouble.

Requirements
============
1. Tested from Raspberry Pi using Python version 2.7
2. A device that can run the Cayenne agent software might be a requirement. (Haven't tried it without one.)
3. A miner like the Antminer S9 that supports the cgminer api.

Steps
============
1. Make sure python is set up on your rpi. If you have problems then make sure you install dependencies. Do a google search.
sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install

2. install mqtt lib. This is a client to communicate with mydevices.com Cayenne back end.
sudo pip install paho-mqtt

3. Create your dashboard by signing up at https://mydevices.com/ and following the prompts. This will set up an agent on your rpi. If you have any issues with the mydevices.com or Cayenne setup then get help on their community forum. Add a device through their site to generate a user id, password id, and client id that you will use in step 5. This will allow you to authenticate to their back end.

4. Download https://github.com/ckolivas/cgminer/blob/master/api-example.py
Save it in any folder on your rpi and rename it minerapi.py
IMPORTANT! Make one small edit to the file. Comment out the following line by putting a # at the beginning of the line.
#response = json.loads(response)
The reason is that we want the raw json string coming from the miner as output, not the python object.

5. Put the file uploadhash.py in the same directory as minerapi.py and then customize with your settings.
Edit the script uploadhash.py with the following info:
 - ip address of your miner
 - mydevices.com Cayenne user, password, and client id from step 2. IMPORTANT! You get this info from the Cayenne dashboard. These values are different than your login and password on that site. 
 - modify the polling interval if you so choose.
 
6. Now run the script, "python uploadhash.py". You can add the script as a cron task by using "crontab -e" and set it up to run @reboot. Google for instructions.
If the script is running correctly then you will see the diagnostics output on the console with your miner stats, hashrate and temp.  
user@raspberrypi:~/mydevices $ python uploadhash.py
13639.64 3 60 55 59
13622.19 3 60 55 60
13634.74 3 61 56 61

7. Check your Cayenne dashboard and configure your widgets. Don't forget to set up Cayenne Alerts from your dashboard to get notified when hashrate falls or temps rise.

Useful Links
====================
The Antminer API is the same as cgminer api. See https://github.com/ckolivas/cgminer/blob/master/API-README

Any feedback is welcome.
Dave
dfoderick@gmail.com
