#!/usr/bin/python
import matplotlib.pyplot as plt
import math

file_1 = open("./0%/data","r")
file_2 = open("./adaptiveTimeout/data","r")
file_3 = open("./20%/data","r")
file_4 = open("./50%/data","r")
file_5 = open("./100%/data","r")

t_1 = eval(file_1.readline())
t_2 = eval(file_2.readline())
t_3 = eval(file_3.readline())
t_4 = eval(file_4.readline())
t_5 = eval(file_5.readline())

pdf_1 = eval(file_1.readline())
pdf_2 = eval(file_2.readline())
pdf_3 = eval(file_3.readline())
pdf_4 = eval(file_4.readline())
pdf_5 = eval(file_5.readline())


cdf_1 = []
cdf_1.append(1);
for i in range(1, len(pdf_1)):
	cdf_1.append(cdf_1[i-1] - pdf_1[i-1])


cdf_2 = []
cdf_2.append(1);
for i in range(1, len(pdf_2)):
	cdf_2.append(cdf_2[i-1] - pdf_2[i-1])

cdf_3 = []
cdf_3.append(1);
for i in range(1, len(pdf_3)):
	cdf_3.append(cdf_3[i-1] - pdf_3[i-1])

cdf_4 = []
cdf_4.append(1);
for i in range(1, len(pdf_4)):
	cdf_4.append(cdf_4[i-1] - pdf_4[i-1])

cdf_5 = []
cdf_5.append(1);
for i in range(1, len(pdf_5)):
	cdf_5.append(cdf_5[i-1] - pdf_5[i-1])

plt.loglog(t_1, cdf_1, 'r--', label = 'default (0% replication)', linewidth=3)
plt.loglog(t_2, cdf_2, 'b',   label = 'adaptive timeout strategy', linewidth=3)
plt.loglog(t_3, cdf_3, 'g+', label = '20% replication', linewidth=3)
plt.loglog(t_4, cdf_4, 'm-.',  label = '50% replication', linewidth=3)
plt.loglog(t_5, cdf_5, 'y*',  label = '100% replication', linewidth=3)

plt.legend(loc = 0, frameon=False, fontsize=17)
plt.grid(True)
plt.xlim((0,150))
plt.ylim((0.001,1))
plt.ylabel('fraction', fontsize=20)
plt.xlabel('tuple processing latency (msec)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=13)
#plt.ylim((0.999,1))
plt.show()
