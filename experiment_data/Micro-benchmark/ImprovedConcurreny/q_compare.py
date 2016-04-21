#!/usr/bin/python
import matplotlib.pyplot as plt
import math

file_1 = open("./default/q_delay","r")
file_2 = open("./Improved/q_delay","r")

t_1 = eval(file_1.readline())
t_2 = eval(file_2.readline())

qdv_1 = eval(file_1.readline())
qdv_2 = eval(file_2.readline())

plt.tick_params(axis='both', which='major', labelsize=15)
plt.plot(t_1, qdv_1, 'r--', linewidth=3,  label ='Storm Default')
plt.plot(t_2, qdv_2, 'b', linewidth=3,  label ='Merging input queue for tasks')
plt.grid(True)
plt.legend(loc = 0, frameon=False, fontsize=17)
plt.xlabel('Time since the activation of the topology (sec)', fontsize=17)
plt.ylabel('queueing delay at bolt (msec)', fontsize=17)
plt.xlim(50,500)
plt.ylim(0,4)

print sum(qdv_1[100:])/len(qdv_1[100:])
print sum(qdv_2[100:])/len(qdv_2[100:])

plt.show()
