#!/usr/bin/python
import matplotlib.pyplot as plt
import math
import sys

c_id = raw_input("exclaimid?")
c_id = "exclaim" + str(c_id)
t = raw_input("choose to see latency change or traffic (load) change, 1 for latency, 2 for traffic")
t = (int)(t)

#result = open("latency", "w")
#result = open("load", "w")
for j in range(1, 6):
	name = "../result_collected/IshuffleInfo_" + str(j) + ".txt"
	file = open(name,"r")

	count = {}
	wait_time = {}

	line = file.readline()
	if (line==""):
		 continue
	
	while (line!=""):
		words = line.split()
		componenet = words[5]
		if(c_id != componenet):
			line = file.readline()
			continue

		time_ptr = (long)(words[8])
		execute_cnt = (int)(words[6])
		wait_lat = (float)(words[7])
		
		count[time_ptr] = execute_cnt
		wait_time[time_ptr] = wait_lat
		line = file.readline()

	if (len(count)==0 or len(wait_time)==0):
		continue

	if(t == 1):
		time_v = sorted(wait_time)
		wt_v = []
		length = len(time_v)
		for i in range(0, length):
			wt_v.append(wait_time[time_v[i]])

		for i in range(1, length):
			time_v[i] = (time_v[i] - time_v[0])/(1000.0)
		time_v[0] = 0
		
		sum = 0
		cnt = 1
		for i in range(0, length):
			if (time_v[i] > 100):
				sum = sum + wt_v[i]
				cnt = cnt + 1
	
		print "storm" + str(j) + " " + str(sum/cnt)
		plt.xlim(0,700)
		plt.ylim(0,20)
		plt.plot(time_v, wt_v)
		#result.write(str(time_v) + '\n')
		#result.write(str(wt_v) + '\n')

	else:
		time_v = sorted(count)
		cnt_v = []
		length = len(time_v)
		for i in range(0, length):
			cnt_v.append(count[time_v[i]])

		for i in range(1, length):
			time_v[i] = (time_v[i] - time_v[0])/(1000.0)
		time_v[0] = 0
		
		print "storm" + str(j) + " " + str(sum(cnt_v))
		plt.xlim(0,700)
		plt.ylim(0,15000)
		plt.plot(time_v, cnt_v)
		#result.write(str(time_v) + '\n')
		#result.write(str(cnt_v) + '\n')

#result.close()
plt.show()

