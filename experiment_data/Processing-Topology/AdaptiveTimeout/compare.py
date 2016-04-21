import matplotlib.pyplot as plt
import math

file_1 = open("./0%/data","r")
file_2 = open("./adaptiveTimeout/data","r")

t_1 = eval(file_1.readline())
t_2 = eval(file_2.readline())


pdf_1 = eval(file_1.readline())
pdf_2 = eval(file_2.readline())


cdf_1 = []
cdf_1.append(1);
for i in range(1, len(pdf_1)):
	cdf_1.append(cdf_1[i-1] - pdf_1[i-1])


cdf_2 = []
cdf_2.append(1);
for i in range(1, len(pdf_2)):
	cdf_2.append(cdf_2[i-1] - pdf_2[i-1])


plt.loglog(t_1, cdf_1, 'r--', label = 'default (0% replication)', linewidth=3)
plt.loglog(t_2, cdf_2, 'b',   label = 'adaptive timeout strategy', linewidth=3)


plt.legend(loc = 0, frameon=False, fontsize=17)
plt.grid(True)
#plt.xlim((0,180))
plt.ylim((0.001,1))
plt.ylabel('fraction', fontsize=20)
plt.xlabel('tuple processing latency (msec)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=13)
#plt.ylim((0.999,1))
plt.show()
