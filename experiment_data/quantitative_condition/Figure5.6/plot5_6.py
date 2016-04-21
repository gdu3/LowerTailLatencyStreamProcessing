import matplotlib.pyplot as plt
import math

x = [17,23.5,36,56,78]
y = [0.78, 9.08, 12.8, 5.8, -6.02]

# Each point of curve x-y represents a pair of experiment, one is Storm default, another one is with ATO technique.
# The collected logfiles are in ato-1 ~ ato-5 directories under ATO directory.
# The values in "y" array are obtained by running script "compare.py" under ato-1 ~ ato-5 directories. (compare the 99% latency of two curve and compute the improvement).
# The values in "x" array are obtained by running lambda / mu, mu can be observed in Storm UI during the experiment, which is about 2.2 ms,
# lambda can be calculated with tuple emission rate from spout tasks, which can be acquired through "plot_sendRate.py" script in "scripts/analysis_scripts".
# If want to run the experiments again, git checkout adaptive-timeout for storm core code,
# add git checkout commit (Topology used by Adaptive Timeout Strategy in Figure 5.6) from branch "quantitative-condition-analysis" for topoloy code.
# add change the tuple emission rate from spout to the followings:
#  In TestWordSpout.java, change if(rand.nextInt(10) < ...) to 
# 	if(rand.nextInt(10) < 3), if(rand.nextInt(10) < 4), if(rand.nextInt(10) < 6), if(rand.nextInt(10) < 8), if(rand.nextInt(10) < 10)
# Each case corresponds to one point in the curve.


a = [20, 57, 67, 77.5]
b = [3.2, 4.6, 10.3, 24.9]

# Each point of curve a-b represents a pair of experiment, one is Storm default, another one is with ICM technique.
# The collected logfiles are in icm-1 ~ icm-4 directories under ICM directory.
# The values in "b" array are obtained by running script "compare.py" under icm-1 ~ icm-4 directories. (compare the 99% latency of two curve and compute the improvement).
# The values in "a" array are obtained by running lambda / mu, mu can be observed in Storm UI during the experiment, which is about 2.2 ms,
# lambda can be calculated with tuple emission rate from spout tasks, which can be acquired through "plot_sendRate.py" script in "scripts/analysis_scripts".
# If want to run the experiments again, git checkout Improved-concurrency-model for storm core code,
# add git checkout commit (Topology used by Improved Concurrency Model in Figure 5.6) from branch "quantitative-condition-analysis" for topoloy code.
# add change the tuple emission rate from spout to the followings:
#  In TestWordSpout.java, change if(rand.nextInt(10) < ...) to 
# 	if(rand.nextInt(10) < 4), if(rand.nextInt(10) < 8), if(rand.nextInt(10) < 9), if(rand.nextInt(10) < 10)
# Each case corresponds to one point in the curve.

plt.grid(True)
plt.xlim((20, 77))
plt.ylim((-5, 30))
plt.plot(x,y,'--', label = 'Adaptive Timeout Strategy', linewidth=3)
plt.plot(a,b, label = 'Improved Concurrency Model', linewidth=3)
plt.legend(loc = 3, frameon=False, fontsize=17)
plt.xlabel('bolt task\'s input queue utilization (%)', fontsize=17)
plt.ylabel('Percentage of Improvement on the 99% latency', fontsize=17)

plt.show()

