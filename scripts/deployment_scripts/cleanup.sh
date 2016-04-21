#!/bin/bash

# save the current directory
cwd=$(pwd)

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "zookeeper" > /dev/null 2>&1 << eeooff
	cd ./ZKData
	sudo rm -R *
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm1" > /dev/null 2>&1 << eeooff
	sudo rm result.tar.gz
	sudo rm -R result	
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm2" > /dev/null 2>&1 << eeooff
	sudo rm -R result	
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm3" > /dev/null 2>&1 << eeooff
	sudo rm -R result	
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm4" > /dev/null 2>&1 << eeooff
	sudo rm -R result	
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm5" > /dev/null 2>&1 << eeooff
	sudo rm -R result	
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm6" > /dev/null 2>&1 << eeooff
	sudo rm -R result	
	cd ~/storm/logs
	sudo rm -R *
	cd ~/storm_datadir
	sudo rm -R *
eeooff

