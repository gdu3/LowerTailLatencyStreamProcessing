#!/usr/bin/python
import matplotlib.pyplot as plt
import math

file_1 = open("./latency","r")

t_11 = eval(file_1.readline())
l_11 = eval(file_1.readline())
t_12 = eval(file_1.readline())
l_12 = eval(file_1.readline())
t_13 = eval(file_1.readline())
l_13 = eval(file_1.readline())

plt.tick_params(axis='both', which='major', labelsize=15)
plt.plot(t_11,l_11,'b--',linewidth=3,  label ='task1')
plt.plot(t_12,l_12,'g',linewidth=3,  label = 'task2')
plt.plot(t_13,l_13,'r:',linewidth=3, label = 'task3')
plt.legend(loc = 1, frameon=False, fontsize=17)
plt.xlabel('Time since the activation of the topology (sec)', fontsize=17)
plt.ylabel('tuple latency of a task (msec)', fontsize=17)
plt.xlim(3,500)
plt.ylim(0,6)
plt.grid(True)

plt.show()
