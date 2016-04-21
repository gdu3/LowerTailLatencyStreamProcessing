gcloud compute copy-files  ./compress  storm2:~ --zone us-central1-b
gcloud compute copy-files  ./compress  storm4:~ --zone us-central1-b

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm2"  'bash -s' < ./assist.sh &
gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm4"  'bash -s' < ./assist.sh &

