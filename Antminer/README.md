Antminer scripts
=================
bmminer.conf is the original configuration from bitmain. Notice that is sets up an API group that everyone has access to read those commands.

bmminer_privileged.conf is for privileged access, for reference.

antminerS9api_privileged.sh
This is the shell script to remotely log into anminer and upgrade API access to privileged access. Be sure to change ip addresses to the miner and the ip address that you will be giving access to.
After running and reboot the api will be in privileged access mode. That will give you the ability to change pools remotely without the delay of restarting.
