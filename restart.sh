killall nginx
killall -9 uwsgi
sleep 3
nohup uwsgi --ini /root/paperweb/uwsgi_config.ini  &
/opt/nginx/sbin/nginx
