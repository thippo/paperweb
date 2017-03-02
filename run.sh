systemctl start iptables.service
sleep 2
systemctl stop iptables.service
nohup /opt/mongodb-linux-x86_64-rhel70-3.4.2/bin/mongod --dbpath=/data/webdb/db &
