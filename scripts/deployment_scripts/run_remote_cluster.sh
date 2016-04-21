#!/bin/bash

# save the current directory
cwd=$(pwd)

echo -n "replace storm-core-0.10.0.jar in remote cluster (y or n) ?"
read text

if [ "$text" = "y" ]
then
	echo -n "Compile the storm again? (y or n) > "
	read t

	if [ "$t" = "y" ]
	then
		cd $cwd/../../storm/storm-core
		mvn clean install -DskipTests=true
	fi

	$cwd/transmit.sh
fi

cd $cwd/../../storm/examples/storm-starter
mvn package

gcloud compute copy-files $cwd/../../storm/examples/storm-starter/target/storm-starter-0.10.0.jar  zookeeper:~/ --zone us-central1-b

$cwd/cleanup.sh
echo "cleanup old logs!!!"

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "zookeeper"  << eeooff
	cd ./storm/bin/
	sudo ./storm jar ../../storm-starter-0.10.0.jar storm.starter.ExclamationTopology test
eeooff

