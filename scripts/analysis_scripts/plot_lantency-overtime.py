#!/usr/bin/python
import matplotlib.pyplot as plt
import math


for i in range(1, 6):
	name = "../result_collected/Acking_" + str(i) + ".txt"
	file = open(name,"r")

	rate = [0 for x in range(900)]
	average = [0 for x in range(900)]

	start_time = {}
	latency = {}

	line = file.readline()
	if (line==""):
		 continue
	
	min_time = 100000000000000

	while (line!=""):
		words = line.split()
		msg_id = words[5]
		lat = int(words[6])
		st = long(words[7])
		start_time[msg_id] = st
		latency[msg_id] = lat
		min_time = min(min_time, st)
		line = file.readline()

	for key in start_time:
		index = (start_time[key] - min_time)/1000
		average[index] = average[index] + latency[key]
		rate[index] = rate[index] + 1

	for i in range(0,900):
		if(rate[i]!=0):
			average[i] = average[i]/rate[i]
	
	plt.plot(range(900), average)
	plt.ylim((0,30))
	plt.xlim((100,900))

plt.xlabel('Time since the activation of the topology (sec)', fontsize=20)
plt.ylabel('Average tuple processing latency (msec)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.show()


