#!/usr/bin/python
import matplotlib.pyplot as plt
import math
from matplotlib import rc,rcParams

def factorial(x):
	ret = 1
	if (x==0):
		return 1
	else:
		for i in range(1,x+1):
			ret = ret * i
		return ret
		
def helper(servers, utilization):
	tmp = servers * utilization
	term_1 = math.pow(tmp, servers)
	term_1 = term_1 / factorial(servers)
	term_2 = 1/(1-utilization)
	term_3 = 0;
	for i in range(0, servers):
		term_3 = term_3 + math.pow(tmp, i)/factorial(i)
	return (term_1 * term_2) / (term_3 + term_1 * term_2)

def average_queuing_time(servers, input_rate, process_rate):
	return helper(servers, input_rate/(servers * process_rate))/(servers * process_rate - input_rate)



service_rate = 1000
for servers in [1,2,4]:
	util = [float(x)/100 for x in range(100)]
	input_rate = []
	input_rate.append(0);
	for i in range(1,100):
		input_rate.append(servers * service_rate * util[i])

	queue_delay = []
	queue_delay.append(0);
	for i in range(1,100):
		queue_delay.append(1000 * average_queuing_time(servers, input_rate[i], service_rate))
	if servers==1:
		plt.plot(range(100), queue_delay, 'r', label = '# server = ' + str(servers), linewidth=3)
	elif servers==2:
		plt.plot(range(100), queue_delay, 'b--', label = '# server = ' + str(servers), linewidth=3)
	else:
		plt.plot(range(100), queue_delay, 'g*', label = '# server = ' + str(servers), linewidth=3)

plt.tick_params(axis='both', which='major', labelsize=15)
plt.legend(loc = 2, frameon=False, fontsize=20)
plt.ylim((0,5))
plt.ylabel('average queuing delay (msec)', fontsize=20)
plt.xlim((0,100))
plt.xlabel('utilization of the queue (%)', fontsize=20)
plt.show()

	
