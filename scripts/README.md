# LowerTailLatencyStreamProcessing scripts

--------------------------------------------------------------------------
						Cluster Setup
--------------------------------------------------------------------------
All the scripts is based on that the cluster is deployed in project named
"storm-1102" on my personal Google Cloud Platform account. 

Therefore, to deploy the cluster in a new project of other account, 
change the project name in all the scripts accordingly.

Or to deploy the cluster on other platform, change "gcloud compute....."
command to "ssh" or "scp". 
If the cluster is deployed on other platform, some parameters in the Topology
code (such as parallelism of spout/bolt, emission rate of spout and etc) may
need to change to obtain a good benchmark, due to difference in VMs' performance.

There are 7 VMs:
zookeeper n1-standard-1 (1 vCPU, 3.75 GB memory),
storm1 n1-standard-2 (2 vCPUs, 7.5 GB memory), 
storm2 n1-standard-2 (2 vCPUs, 7.5 GB memory), 
storm3 n1-standard-2 (2 vCPUs, 7.5 GB memory), 
storm4 n1-standard-2 (2 vCPUs, 7.5 GB memory),
storm5 n1-standard-2 (2 vCPUs, 7.5 GB memory),
storm6 n1-standard-1 (1 vCPU, 3.75 GB memory)

In the scripts, cluster 1 refers to (storm1, storm2, storm3, storm4, storm5)
cluster 2 refers to (storm1, storm2, storm3, storm4, storm5)

the zookeeper node performs the role of "Zookeeper" and "Nimbus"
the storm1-6 performs the role of "worker"

In all VMs, install JVM and apache2 (run scripts/deployment_scripts/install/install_jvm.sh
on all the VMs.) 
And setup Apache Storm according to http://storm.apache.org/releases/0.10.0/Setting-up-a-Storm-cluster.html

After setup, the directory structure under the "~" directory of zookeeper VM is:
storm storm_datadir ZKData zookeeper
After setup, the directory structure under the "~" directory of storm1-storm6 VM is:
storm storm_datadir

In all VMs, 
the /etc/hosts file stores the mappings between the names of VMs and their ip addresses.
Under the /var/www/html/ directory, create a soft link called "home" linked to directory "~".


--------------------------------------------------------------------------
						Brief Description of script files
--------------------------------------------------------------------------
Under deployment_scripts directory:
(1) deploy_daemon.sh: to start the zookeeper, nimbus, supervisor daemon processes.

(2) run_remote_clusher.sh: to run a topology code on the Storm cluster.

(3) transmit.sh: to copy the local compiled storm jar files to remote cluster.

(4) collect_result.sh: to collect the log files from the remote cluster to local computer.

(5) cleanup.sh: to delete the data for each run to avoid interference between runs.

(6) compress-task: a compression programs serving as exteral process in Experiment
Scenario-B of latency-based load balance.

Under analysis_scripts directory:
(1) plot_distribution.py: to plot the latency distribution of the tuples.

(2) plot_distributionWithAdaptiveTimeout.py: to plot the latency distribution
of the tuples with Adaptive Timeout Strategy.

(3) plot_distributionWithReplication.py: to plot the latency distribution
of the tuples with replication.

(4) plot_lantency-overtime.py: to plot how the average tuple latency changes
over time. It can be used to inspect when the cluster finish initial startup phase.
If the spout emission rate is constant over time, the variation of average
latency should be small after initial startup phase, unless the VMs are
experiencing performance fluctuation.

(5) plot_latencyOrTraffic_change.py: to plot how loading Or latency of tasks
changes over time. It is used in the experiments of latency-based load balance.

(6) plot_queueingDelay.py: to plot the average queueing delay of the bolt.
It is used in the experiments of improved concurrency model of worker process.

(7) plot_queuingThery.py: to plot the queueing delay according to M/M/c model in
queueing theory.

(8) plot_sendRate.py: to plot the spouts' tuple emission rate.

(9) plot_Timeout.py: to plot the how the timeout value in Adaptive Timeout
Strategy changes over time.


-------------------------------------------------------------------------------
						Steps to generate plots
-------------------------------------------------------------------------------
cwd=$(pwd) # save the current directory

-----------------------
	Thesis Figure 3.4
-----------------------
cd $cwd/analysis_scripts/
./plot_queuingThery.py


-----------------------
	Thesis Figure 5.1
-----------------------
(Option 1): generate plot from collected raw logfiles
-------------------------------------------------------
cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/AdaptiveTimeout/0%/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/0%/


cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/AdaptiveTimeout/20%/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distributionWithReplication.py (300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/20%/


cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/AdaptiveTimeout/50%/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distributionWithReplication.py (200)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/50%/


cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/AdaptiveTimeout/100%/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distributionWithReplication.py (200)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/100%/


cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/AdaptiveTimeout/adaptiveTimeout/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distributionWithAdaptiveTimeout.py (300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/adaptiveTimeout/

cd ../experiment_data/Micro-benchmark/AdaptiveTimeout
./compare.py


(Option 2): run the experiments and generate new logfiles and plot
-------------------------------------------------------------------
cd $cwd
cd ../storm/storm-core/src
git checkout adaptive-timeout


cd $cwd
cd ../storm/examples/storm-starter/src
git checkout adaptive-timeout-strategy-topotlogy
cd ./jvm/storm/starter
In ExclamationTopology.java "conf.setEnableTimeoutAdjustment(true);" line, 
change true to false
cd $cwd/deployment_scripts
./deploy_daemon.sh (1)
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/0%/


cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
In ExclamationTopology.java "conf.setEnableTimeoutAdjustment(true);" line,
keep the parameter to be true
cd $cwd/deployment_scripts
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distributionWithAdaptiveTimeout.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/adaptiveTimeout/


cd $cwd
cd ../storm/storm-core/src
git checkout replication


cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
comment "conf.setEnableTimeoutAdjustment(true);" in ExclamationTopology.java
and uncomment "//conf.setReplicationRatio(0.5);" and change 0.5 to 0.2
cd $cwd/deployment_scripts
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distributionWithReplication.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/20%/


cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
comment "conf.setEnableTimeoutAdjustment(true);" in ExclamationTopology.java
and uncomment "//conf.setReplicationRatio(0.5);"
cd $cwd/deployment_scripts
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distributionWithReplication.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/50%/


cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
comment "conf.setEnableTimeoutAdjustment(true);" in ExclamationTopology.java
and uncomment "//conf.setReplicationRatio(0.5);" change 0.5 to 1
cd $cwd/deployment_scripts
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distributionWithReplication.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/AdaptiveTimeout/100%/

cd ../experiment_data/Micro-benchmark/AdaptiveTimeout
./compare.py


-------------------------------
	Thesis Figure 5.2 & 5.3
-------------------------------

(Option 1): generate plot from collected raw logfiles
-------------------------------------------------------
cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/ImprovedConcurreny/default/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (220)
./plot_queueingDelay.py (2)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/ImprovedConcurreny/default/
mv ./analysis_scripts/q_delay ../experiment_data/Micro-benchmark/ImprovedConcurreny/default/


cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/ImprovedConcurreny/Improved/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (220)
./plot_queueingDelay.py (2)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/ImprovedConcurreny/Improved/
mv ./analysis_scripts/q_delay ../experiment_data/Micro-benchmark/ImprovedConcurreny/Improved/

cd ../experiment_data/Micro-benchmark/ImprovedConcurreny
./compare.py
./q_compare.py


(Option 2): run the experiments and generate new logfiles and plot
-------------------------------------------------------------------
cd $cwd
cd ../storm/storm-core/src
git checkout Improved-concurrency-model


cd $cwd
cd ../storm/examples/storm-starter/src
git checkout Improved-concurrency-model-topology
cd $cwd/deployment_scripts
./deploy_daemon.sh (1)
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
./plot_queueingDelay.py (1~5)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/ImprovedConcurreny/Improved/
mv ./analysis_scripts/q_delay ../experiment_data/Micro-benchmark/ImprovedConcurreny/Improved/


cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
In ExclamationTopology.java, change the parameter to "false"
in "conf.setImprovedConcurrencyModel(true);"
cd $cwd/deployment_scripts
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
./plot_queueingDelay.py (1~5)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/Micro-benchmark/ImprovedConcurreny/default/
mv ./analysis_scripts/q_delay ../experiment_data/Micro-benchmark/ImprovedConcurreny/default/


cd ../experiment_data/Micro-benchmark/ImprovedConcurreny
./compare.py
./q_compare.py


---------------------------------------
	Thesis Figure 5.4 & 5.5
---------------------------------------

(Option 1): generate plot from collected raw logfiles
-------------------------------------------------------
cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/LatencyBasedLoadBalance/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
./plot_latencyOrTraffic_change.py (2,1) (uncomment the lines "result=open(\"latency\",..) result.write..")
./plot_latencyOrTraffic_change.py (2,2) (uncomment the lines "result=open(\"load\",..) result.write..")

cd $cwd
mv ./analysis_scripts/data 		../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/LatencyBasedLoadBalance/
mv ./analysis_scripts/latency 	../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/
mv ./analysis_scripts/load 		../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/

cd ../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A
./plot_load.py
./plot_latency.py


(Option 2): run the experiments and generate new logfiles and plot
-------------------------------------------------------------------
cd $cwd
cd ../storm/storm-core/src
git checkout latency-based_loadBalance


cd $cwd
cd ../storm/examples/storm-starter/src
git checkout latencyBasedLoadBalance-scenario-A
cd $cwd/deployment_scripts
./deploy_daemon.sh (1)
./run_remote_cluster.sh (y,y) (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
./plot_latencyOrTraffic_change.py (1~5,1) (uncomment the lines "result=open(\"latency\",..) result.write..")
./plot_latencyOrTraffic_change.py (1~5,2) (uncomment the lines "result=open(\"load\",..) result.write..")

cd $cwd
mv ./analysis_scripts/data 		../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/LatencyBasedLoadBalance/
mv ./analysis_scripts/latency 	../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/
mv ./analysis_scripts/load 		../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A/

cd ../experiment_data/Micro-benchmark/LatencyBasedLoadBalance/scenario-A
./plot_load.py
./plot_latency.py

---------------------------------------
	Thesis Figure 5.6
---------------------------------------
cd ../experiment_data/quantitative_condition/Figure5.6
python plot5_6.py

---------------------------------------
	Thesis Figure 5.7
---------------------------------------
cd ../experiment_data/quantitative_condition/Figure5.7
python plot5_7.py

---------------------------------------
	Thesis Figure 5.9 (a)
---------------------------------------
(Option 1): generate plot from collected raw logfiles
-------------------------------------------------------
cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/PageLoad-Topology/AdaptiveTimeout/0%/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
cd $cwd
mv ./analysis_scripts/data 		../experiment_data/PageLoad-Topology/AdaptiveTimeout/0%/

cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/PageLoad-Topology/AdaptiveTimeout/adaptiveTimeout/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distributionWithAdaptiveTimeout.py (200)
cd $cwd
mv ./analysis_scripts/data 		../experiment_data/PageLoad-Topology/AdaptiveTimeout/adaptiveTimeout/

cd ../experiment_data/PageLoad-Topology/AdaptiveTimeout/
python compare.py

(Option 2): run the experiments and generate new logfiles and plot
-------------------------------------------------------------------
cd $cwd
cd ../storm/storm-core/src
git checkout adaptive-timeout

cd $cwd
cd ../storm/examples/storm-starter/src
git checkout PageLoad-Process-Topology
git check commit (Page Load Topology benchmark for Adaptive timeout strategy) -b tt
cd ./jvm/storm/starter
In PageLoadTopology.java "conf.setEnableTimeoutAdjustment(true);" line, 
change true to false
cd $cwd/deployment_scripts
./deploy_daemon.sh (1)
./run_remote_cluster.sh (y,y) (change the "ExclamationTopology" to "PageLoadTopology") (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/PageLoad-Topology/AdaptiveTimeout/0%/

cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
In PageLoadTopology.java "conf.setEnableTimeoutAdjustment(true);" line,
keep the parameter to be true
cd $cwd/deployment_scripts
./run_remote_cluster.sh (y,y) (change the "ExclamationTopology" to "PageLoadTopology") (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distributionWithAdaptiveTimeout.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/PageLoad-Topology/AdaptiveTimeout/adaptiveTimeout/

cd ../experiment_data/PageLoad-Topology/AdaptiveTimeout/
python compare.py

---------------------------------------
	Thesis Figure 5.9 (b)
---------------------------------------
The step for generating 5.9 (b) is almost the same with 5.9 (a)
except all of path information is changed from "PageLoad-Topology" to "Processing-Topology"
Also the benchmark topplogy is the commit "Processing Topology benchmark for Adaptive timeout strategy" from
branch "PageLoad-Process-Topology".


---------------------------------------
	Thesis Figure 5.10 (a)
---------------------------------------
(Option 1): generate plot from collected raw logfiles
-------------------------------------------------------
cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/PageLoad-Topology/ImprovedConcurreny/default/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
cd $cwd
mv ./analysis_scripts/data 		../experiment_data/PageLoad-Topology/ImprovedConcurreny/default/

cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/PageLoad-Topology/ImprovedConcurreny/improved/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
cd $cwd
mv ./analysis_scripts/data 		../experiment_data/PageLoad-Topology/ImprovedConcurreny/improved/

cd ../experiment_data/PageLoad-Topology/ImprovedConcurreny/
python compare.py


(Option 2): run the experiments and generate new logfiles and plot
-------------------------------------------------------------------
cd $cwd
cd ../storm/storm-core/src
git checkout Improved-concurrency-model

Add storm.scheduler: "backtype.storm.scheduler.GroupingScheduler" to the storm.yaml file in zookeeper node.
Add supervisor.scheduler.meta:
  	  groupId: "i"
    to the storm.yaml file in stormi node, where i is from 1 to 5.
After this set of experiments, change storm.yaml files to their original state.

cd $cwd
cd ../storm/examples/storm-starter/src
git checkout PageLoad-Process-Topology
git log
git check commit (Page Load Topology benchmark for improved concurrency model) -b tt
cd ./jvm/storm/starter
In PageLoadTopology.java "conf.setImprovedConcurrencyModel(true);" line, 
change true to false
cd $cwd/deployment_scripts
./deploy_daemon.sh (1)
./run_remote_cluster.sh (y,y) (change the "ExclamationTopology" to "PageLoadTopology") (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/PageLoad-Topology/ImprovedConcurreny/default/

cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
In PageLoadTopology.java "conf.setImprovedConcurrencyModel(true);" line,
keep the parameter to be true
cd $cwd/deployment_scripts
/run_remote_cluster.sh (y,y) (change the "ExclamationTopology" to "PageLoadTopology") (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
/plot_distribution.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/PageLoad-Topology/ImprovedConcurreny/improved/

cd ../experiment_data/PageLoad-Topology/ImprovedConcurreny/
python compare.py

---------------------------------------
	Thesis Figure 5.10 (b)
---------------------------------------
The step for generating 5.10 (b) is almost the same with 5.10 (a)
except all of path information is changed from "PageLoad-Topology" to "Processing-Topology"
Also the benchmark topplogy is the commit "Processing Topology benchmark for improved concurrency model" from
branch "PageLoad-Process-Topology".


---------------------------------------
	Thesis Figure 5.11 (a)
---------------------------------------
(Option 1): generate plot from collected raw logfiles
-------------------------------------------------------
cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/default/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
cd $cwd
mv ./analysis_scripts/data 		../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/default/

cd $cwd
rm -r ./result_collected
mkdir result_collected
cp ../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/LatencyBasedLoadBalance/result.tar.gz ./result_collected
cd ./result_collected
tar xzf result.tar.gz
mv ./result/* ./
rm -R result
cd $cwd/analysis_scripts
./plot_distribution.py (200)
cd $cwd
mv ./analysis_scripts/data 		../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/LatencyBasedLoadBalance/

cd ../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/
python compare.py


(Option 2): run the experiments and generate new logfiles and plot
-------------------------------------------------------------------
cd $cwd
cd ../storm/storm-core/src
git checkout latency-based_loadBalance

cd $cwd
cd ../storm/examples/storm-starter/src
git checkout PageLoad-Process-Topology
git log
git check commit (Page Load Topology benchmark for latency-based load balance scenario-c) -b tt
cd ./jvm/storm/starter
In PageLoadTopology.java "conf.setIShuffleGroupingEnable(1);" line, 
change 1 to 0
cd $cwd/deployment_scripts
./deploy_daemon.sh (2)
./run_remote_cluster.sh (y,y) (change the "ExclamationTopology" to "PageLoadTopology") (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
./plot_distribution.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/default/

cd $cwd
cd ../storm/examples/storm-starter/src/jvm/storm/starter
In PageLoadTopology.java "conf.setIShuffleGroupingEnable(1);" line, 
keep the parameter to be 1
cd $cwd/deployment_scripts
/run_remote_cluster.sh (y,y) (change the "ExclamationTopology" to "PageLoadTopology") (let it run for at least 10 minutes)
kill the topology from Storm UI
./collect_result.sh
cd $cwd/analysis_scripts
/plot_distribution.py (200 ~ 300)
cd $cwd
mv ./analysis_scripts/data ../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/LatencyBasedLoadBalance/

cd ../experiment_data/PageLoad-Topology/LatencyBasedLoadBalance/
python compare.py

---------------------------------------
	Thesis Figure 5.11 (b)
---------------------------------------
The step for generating 5.11 (b) is almost the same with 5.11 (a)
except all of path information is changed from "PageLoad-Topology" to "Processing-Topology"
Also the benchmark topplogy is the commit "Processing Topology benchmark for latency-based load balance scenario-c" from
branch "PageLoad-Process-Topology".










