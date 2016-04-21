import matplotlib.pyplot as plt
import math

x = [19.6, 60, 76.24, 88.79]
y = [-9, 3.3, 14.4, 76.2]

# Each point of curve x-y represents a pair of experiment, one is Storm default, another one is with LLB technique.
# The collected logfiles are in llb-1 ~ llb-4 directories under LLB directory.
# The values in "y" array are obtained by running script "compare.py" under llb-1 ~ llb-4 directories. (compare the 99% latency of two curve and compute the improvement).
# The values in "x" array are obtained by running "sar 2 100000 > output" on VM "storm-6" during the experiments. The collected statistics are also in llb-1/default/output ~ llb-4/default/output
# If want to run the experiments again, git checkout latency-based_loadBalance for storm core code,
# add git checkout commit (Topology used by latency-based load balance in Figure 5.7) from branch "quantitative-condition-analysis" for topoloy code.
# add change the tuple emission rate from spout to the followings:
#  In TestWordSpout.java, change if(rand.nextInt(10) < ...) to 
# 	if(rand.nextInt(10) < 2), if(rand.nextInt(10) < 7), if(rand.nextInt(10) < 8), if(rand.nextInt(10) < 9)
# Each case corresponds to one point in the curve.

a = [27.68, 35.4, 40.65, 46.7, 57.33]
b = [2.3, 10, 19.1, 7.1, -27.7]

# Each point of curve a-b represents a pair of experiment, one is Storm default, another one is with ATO technique.
# The collected logfiles are in ato-1 ~ ato-5 directories under ATO directory.
# The values in "b" array are obtained by running script "compare.py" under ato-1 ~ ato-5 directories. (compare the 99% latency of two curve and compute the improvement).
# The values in "x" array are obtained by running "sar 2 100000 > output" on VM "storm-6" during the experiments. The collected statistics are also in ato-1/default/output ~ ato-5/default/output
# If want to run the experiments again, git checkout adaptive-timeout for storm core code,
# add git checkout commit (Topology used by Adaptive Timeout Strategy in Figure 5.7) from branch "quantitative-condition-analysis" for topoloy code.
# add change the tuple emission rate from spout to the followings:
#  In TestWordSpout.java, change if(rand.nextInt(10) < ...) to 
# 	if(rand.nextInt(10) < 4), if(rand.nextInt(10) < 5), if(rand.nextInt(10) < 6), if(rand.nextInt(10) < 7), if(rand.nextInt(10) < 8)
# Each case corresponds to one point in the curve.

plt.grid(True)
plt.xlim((28, 88))
plt.ylim((-20, 80))

plt.plot(a,b,'--', label = 'Adaptive Timeout Strategy', linewidth=3)
plt.plot(x,y, label = 'Latency-based Load Balance', linewidth=3)
plt.legend(loc = 0, frameon=False, fontsize=17)
plt.xlabel('CPU utilization of the \'n1-standard-1\' VM (%)', fontsize=17)
plt.ylabel('Percentage of Improvement on the 99% latency', fontsize=17)

plt.show()

