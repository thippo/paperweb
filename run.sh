systemctl start iptables.service
sleep 2
systemctl stop iptables.service
nohup /opt/mongodb-linux-x86_64-rhel70-3.2.8/bin/mongod --dbpath=/root/data/db &
