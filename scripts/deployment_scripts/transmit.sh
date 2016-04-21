# save the current directory
cwd=$(pwd)

gcloud compute copy-files $cwd/../../storm/storm-core/target/storm-core-0.10.0.jar  zookeeper:~/ --zone us-central1-b
	
gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm1" > /dev/null 2>&1 << eeooff
	wget http://zookeeper/home/storm-core-0.10.0.jar
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm2" > /dev/null 2>&1 << eeooff
	wget http://zookeeper/home/storm-core-0.10.0.jar
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm3" > /dev/null 2>&1 << eeooff
	wget http://zookeeper/home/storm-core-0.10.0.jar
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm4" > /dev/null 2>&1 << eeooff
	wget http://zookeeper/home/storm-core-0.10.0.jar
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm5" > /dev/null 2>&1 << eeooff
	wget http://zookeeper/home/storm-core-0.10.0.jar
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm6" > /dev/null 2>&1 << eeooff
	wget http://zookeeper/home/storm-core-0.10.0.jar
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "zookeeper" > /dev/null 2>&1 << eeooff
	sudo mv ./storm-core-0.10.0.jar ~/storm/lib
eeooff


