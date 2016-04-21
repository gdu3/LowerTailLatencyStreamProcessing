#!/usr/bin/python
import matplotlib.pyplot as plt
import math


timeout = {}

start_timeout_adjustment = 120

for i in range(1, 6):
	name = "../result_collected/TimeoutV_" + str(i) + ".txt"
	file = open(name,"r")
	
	timeout = {}
	line = file.readline()
	if (line ==""):
		 continue

	while (line !=""):
		words = line.split()
		value = int(words[5])
		time  = int(words[6])
			
		timeout[time] = value
		
		line = file.readline()

	
	time_v = sorted(timeout)
	tov = []

	length = len(time_v)

	for i in range(0, length):
		tov.append(timeout[time_v[i]])

	for i in range(1, length):
		time_v[i] = (time_v[i] - time_v[0])/(1000.0) + start_timeout_adjustment
	
	time_v[0] = 0 + start_timeout_adjustment

	plt.plot(time_v, tov)

plt.show()

