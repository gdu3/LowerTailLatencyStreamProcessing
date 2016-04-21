#!/usr/bin/python
import matplotlib.pyplot as plt
import math
import sys

t = raw_input("want to see which machine?")
t = (int)(t)


name = "../result_collected/RecvQDelay_" + str(t) + ".txt"
file = open(name,"r")

queuing_delay = {}

line = file.readline()
while (line!=""):
	words = line.split()
	executor_id = words[7]
	q_delay = (float)(words[5])
	time_ptr = (long)(words[6])

	if not (executor_id in queuing_delay):
		queuing_delay[executor_id] = {}

	delay = queuing_delay[executor_id]
	delay[time_ptr] = q_delay
	line = file.readline()

first = True
for executor_id in queuing_delay:
	delay = queuing_delay[executor_id]
	time_v = sorted(delay)
	qd_v = []
	length = len(time_v)
	for i in range(0, length):
		qd_v.append(delay[time_v[i]])

	for i in range(1, length):
		time_v[i] = (time_v[i] - time_v[0])/(1000.0)
	time_v[0] = 0

	sum = 0
	cnt = 0
	for i in range(1, length):
		if(time_v[i]>=100):
			sum += qd_v[i]
			cnt += 1
			
	print (float)(sum)/cnt
	plt.xlim(100, 700)
	plt.ylim(0,5)
	plt.plot(time_v, qd_v)
	
	if first:
		first = False
		result = open("q_delay", "w")
		result.write(str(time_v) + '\n')
		result.write(str(qd_v) + '\n')
		result.close()
	
plt.show()


