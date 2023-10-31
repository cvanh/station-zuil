#/usr/bin/env bash

#echo "status of container"
#docker ps -f name=station_db


echo 'please enter the password for the postgres user "docker" this "example"'
# dump the database from the container to local
pg_dump \
-h 127.0.0.1 \
-U docker \
-p 8306 \
docker > \
$(dirname $0)/dump.sql