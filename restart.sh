killall nginx
killall -9 uwsgi
sleep 3
nohup uwsgi --ini /data/paperweb/uwsgi_config.ini  &
/usr/local/nginx/sbin/nginx
