#!/bin/bash

#cd ./ZKData
#sudo rm -R *
#cd /home/gdu3/storm
#sudo rm -R logs
#cd /home/gdu3/storm_datadir
#sudo rm -R *

cd ~/zookeeper/bin/
./zkServer.sh start
cd ~/storm/bin
./storm nimbus &
./storm ui &
