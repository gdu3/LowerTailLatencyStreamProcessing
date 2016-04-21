#!/bin/bash

# save the current directory
cwd=$(pwd)

echo -n "cluster 1 (storm1,2,3,4,5) or cluster 2 (storm1,2,3,4,6)?"
read text

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "zookeeper" 'bash -s' < $cwd/deploy/master.sh &

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm1" 'bash -s' < $cwd/deploy/workers.sh &
gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm2" 'bash -s' < $cwd/deploy/workers.sh &
gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm3" 'bash -s' < $cwd/deploy/workers.sh &
gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm4" 'bash -s' < $cwd/deploy/workers.sh &

if [ "$text" = "1" ]
then
	gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm5" 'bash -s' < $cwd/deploy/workers.sh &
else
	gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm6" 'bash -s' < $cwd/deploy/workers.sh &
fi
