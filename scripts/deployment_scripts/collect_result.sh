# save the current directory
cwd=$(pwd)

echo -n "collect result from cluster 1 (storm1,2,3,4,5) or cluster 2 (storm1,2,3,4,6)?"
read text

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm1" > /dev/null 2>&1 << eeooff
	mkdir result	
	cd storm/logs/	
	grep  "Acking"   test*    > ~/result/Acking_1.txt
	grep  "Failing"  test*    > ~/result/Failing_1.txt
	grep  "TimeoutV" test*    > ~/result/TimeoutV_1.txt
	grep  "IshuffleInfo" test* > ~/result/IshuffleInfo_1.txt
	grep  "RecvQDelay"   test* > ~/result/RecvQDelay_1.txt
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm2" > /dev/null 2>&1 << eeooff
	mkdir result	
	cd storm/logs/	
	grep  "Acking"   test*  > ~/result/Acking_2.txt
	grep  "Failing"  test*  > ~/result/Failing_2.txt
	grep  "TimeoutV" test*  > ~/result/TimeoutV_2.txt
	grep  "IshuffleInfo" test* > ~/result/IshuffleInfo_2.txt
	grep  "RecvQDelay"   test* > ~/result/RecvQDelay_2.txt
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm3" > /dev/null 2>&1 << eeooff
	mkdir result	
	cd storm/logs/	
	grep  "Acking"   test*  > ~/result/Acking_3.txt
	grep  "Failing"  test*  > ~/result/Failing_3.txt
	grep  "TimeoutV" test*  > ~/result/TimeoutV_3.txt
	grep  "IshuffleInfo" test* > ~/result/IshuffleInfo_3.txt
	grep  "RecvQDelay"   test* > ~/result/RecvQDelay_3.txt
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm4" > /dev/null 2>&1 << eeooff
	mkdir result	
	cd storm/logs/	
	grep  "Acking"    test* > ~/result/Acking_4.txt
	grep  "Failing"   test* > ~/result/Failing_4.txt
	grep  "TimeoutV"  test* > ~/result/TimeoutV_4.txt
	grep  "IshuffleInfo" test* > ~/result/IshuffleInfo_4.txt
	grep  "RecvQDelay"   test* > ~/result/RecvQDelay_4.txt
eeooff

if [ "$text" = "1" ]
then
	$cwd/result_collect_assist/collect_storm5.sh
else
	$cwd/result_collect_assist/collect_storm6.sh
fi

cd $cwd/../
rm -r result_collected
mkdir result_collected


gcloud compute copy-files storm1:~/result.tar.gz $cwd/../result_collected  --zone us-central1-b
cd $cwd/../result_collected/
tar xzf result.tar.gz
mv ./result/* ./
rm -R result

