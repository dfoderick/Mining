#shell command to upgrade Antminer to privileged access
ssh root@ipaddress.of.your.miner << EOF
cd /config
cp bmminer.conf bmminer_last.conf
chmod u=rw bmminer.conf
sed -i 's_^\("api-allow" : \).*_\1"W:your.ip.address,W:192.168.1.0/24,A:0/0"_' bmminer.conf
chmod u=r bmminer.conf
reboot
EOF
