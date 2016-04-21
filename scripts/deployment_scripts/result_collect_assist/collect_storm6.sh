gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm6" > /dev/null 2>&1 << eeooff
	mkdir result	
	cd storm/logs/	
	grep "Acking"   test* > ~/result/Acking_5.txt
	grep "Failing"  test* > ~/result/Failing_5.txt
	grep "TimeoutV" test* > ~/result/TimeoutV_5.txt
	grep "IshuffleInfo" test* > ~/result/IshuffleInfo_5.txt
	grep  "RecvQDelay"   test* > ~/result/RecvQDelay_5.txt
eeooff

gcloud compute --project "storm-1102" ssh --zone "us-central1-b" "storm1" > /dev/null 2>&1 << eeooff
	cd result
	wget http://storm2/home/result/Acking_2.txt
	wget http://storm2/home/result/Failing_2.txt
	wget http://storm2/home/result/TimeoutV_2.txt
	wget http://storm2/home/result/IshuffleInfo_2.txt
	wget http://storm2/home/result/RecvQDelay_2.txt

	wget http://storm3/home/result/Acking_3.txt
	wget http://storm3/home/result/Failing_3.txt
	wget http://storm3/home/result/TimeoutV_3.txt
	wget http://storm3/home/result/IshuffleInfo_3.txt
	wget http://storm3/home/result/RecvQDelay_3.txt

	wget http://storm4/home/result/Acking_4.txt
	wget http://storm4/home/result/Failing_4.txt
	wget http://storm4/home/result/TimeoutV_4.txt
	wget http://storm4/home/result/IshuffleInfo_4.txt
	wget http://storm4/home/result/RecvQDelay_4.txt

	wget http://storm6/home/result/Acking_5.txt
	wget http://storm6/home/result/Failing_5.txt
	wget http://storm6/home/result/TimeoutV_5.txt
	wget http://storm6/home/result/IshuffleInfo_5.txt
	wget http://storm6/home/result/RecvQDelay_5.txt
	wget http://storm6/home/output.txt

	cd ~
	tar czf result.tar.gz result
eeooff
