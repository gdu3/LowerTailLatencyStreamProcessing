#!/usr/bin/python
import matplotlib.pyplot as plt
import math


for i in range(1, 6):
	name = "../result_collected/Acking_" + str(i) + ".txt"
	file = open(name,"r")

	rate = [0 for x in range(900)]
	start_time = {}

	line = file.readline()
	if (line==""):
		 continue
	
	min_time = 100000000000000

	while (line!=""):
		words = line.split()
		msg_id = words[5]
		st = long(words[7])
		start_time[msg_id] = st
		min_time = min(min_time, st)
		line = file.readline()

	for key in start_time:
		index = (start_time[key] - min_time)/1000
		rate[index] = rate[index] + 1

	plt.plot(range(900), rate)

plt.show()

