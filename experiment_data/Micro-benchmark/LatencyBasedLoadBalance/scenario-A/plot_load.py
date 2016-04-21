#!/usr/bin/python
import matplotlib.pyplot as plt
import math

file_2 = open("./load","r")

t_21 = eval(file_2.readline())
l_21 = eval(file_2.readline())
t_22 = eval(file_2.readline())
l_22 = eval(file_2.readline())
t_23 = eval(file_2.readline())
l_23 = eval(file_2.readline())

for i in range(0,len(l_21)):
	l_21[i] = l_21[i] / 3

for i in range(0,len(l_22)):
	l_22[i] = l_22[i] / 3

for i in range(0,len(l_23)):
	l_23[i] = l_23[i] / 3


plt.tick_params(axis='both', which='major', labelsize=15)
plt.plot(t_21,l_21,'b--',linewidth=3,  label ='task1')
plt.plot(t_22,l_22,'g',linewidth=3,  label = 'task2')
plt.plot(t_23,l_23,'r:',linewidth=3, label = 'task3')
plt.legend(loc = 0, frameon=False, fontsize=17)
plt.xlabel('Time since the activation of the topology (sec)', fontsize=17)
plt.ylabel('# tuple processed by a task per sec', fontsize=17)
plt.xlim(10,500)
plt.ylim(0,2500)
plt.grid(True)

plt.show()
