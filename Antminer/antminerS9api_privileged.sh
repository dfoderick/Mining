#shell command to upgrade Antminer to privileged access
ssh root@ipaddress.of.your.miner << EOF
cd /config
cp bmminer.conf bmminer_last.conf
chmod u=rw bmminer.conf
sed -i 's_^\("api-allow" : \).*_\1"W:your.remote.ip.address,W:192.168.0.1/16,A:0/0",_' bmminer.conf
chmod u=r bmminer.conf
reboot
EOF
