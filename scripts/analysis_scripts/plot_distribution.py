#!/usr/bin/python

import matplotlib.pyplot as plt
import math
import numpy as np

bt = raw_input("want to see result after how many sec?")
stable_threshold = (int)(bt) * 1000

dict = {}
latency = {}
start_time = {}

for i in range(1, 6):
	name = "../result_collected/Acking_" + str(i) + ".txt"
	file = open(name,"r")

	latency = {}
	start_time = {}
	line = file.readline()
	if (line==""):
		 continue
	
	min_time = 100000000000000
	while (line!=""):
		words = line.split()
		msg_id = words[5]
		lat = int(words[6])
		st = long(words[7])
		if msg_id in latency:
			msg_id = "1_" + msg_id

		latency[msg_id] = lat
		start_time[msg_id] = st
		min_time = min(min_time, st)
		line = file.readline()

	baseline = min_time + stable_threshold

	for key in latency:
		if (start_time[key] < baseline):
			continue

		num = latency[key]
		if (num in dict):
			dict[num] = dict[num] + 1
		else:
			dict[num] = 1


time = sorted(dict.keys())

pdf = []

average = 0
sum = 0
length = len(time)
for i in range(0, length):
	pdf.append(dict[time[i]])
	sum = sum + dict[time[i]]
	average = average + time[i] * dict[time[i]]

print "count: " + str(sum)
average = average / (float)(sum)
print "average " + str(average)

for i in range(0, length):
	pdf[i] = pdf[i]/float(sum);

cdf = []
cdf.append(1);
for i in range(1, length):
	cdf.append(cdf[i-1] - pdf[i-1])

#plt.plot(time, pdf)
plt.loglog(time, cdf)
plt.grid(True)
plt.ylim((0.001,1))
result = open("data", "w")
result.write(str(time) + '\n')
result.write(str(pdf) + '\n')
result.write(str(sum) + '\n')
result.write(str(average) + '\n')
result.close()
plt.show()



