#!/bin/bash
#
#
#
# Traces:
#    cassandra_phase0_4T
#    cassandra_phase1_4T
#    cassandra_phase2_4T
#    cassandra_phase3_4T
#    cassandra_phase4_4T
#    cassandra_phase5_4T
#
#
# Experiments:
#    coop_pythia: --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=$(PYTHIA_HOME)/config/coop_pythia.ini --dram_io_freq=2400
#
#
#
#
/pref/Pythia/bin/perceptron-multi-coop_pythia-no-ship-4core --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=/pref/Pythia/config/coop_pythia.ini --dram_io_freq=2400 --knob_cloudsuite=true -traces /pref/Pythia/CASSANDRA/traces/cassandra_phase0_core0.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase0_core1.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase0_core2.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase0_core3.trace.xz > cassandra_phase0_4T_coop_pythia.out 2>&1
/pref/Pythia/bin/perceptron-multi-coop_pythia-no-ship-4core --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=/pref/Pythia/config/coop_pythia.ini --dram_io_freq=2400 --knob_cloudsuite=true -traces /pref/Pythia/CASSANDRA/traces/cassandra_phase1_core0.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase1_core1.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase1_core2.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase1_core3.trace.xz > cassandra_phase1_4T_coop_pythia.out 2>&1
/pref/Pythia/bin/perceptron-multi-coop_pythia-no-ship-4core --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=/pref/Pythia/config/coop_pythia.ini --dram_io_freq=2400 --knob_cloudsuite=true -traces /pref/Pythia/CASSANDRA/traces/cassandra_phase2_core0.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase2_core1.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase2_core2.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase2_core3.trace.xz > cassandra_phase2_4T_coop_pythia.out 2>&1
/pref/Pythia/bin/perceptron-multi-coop_pythia-no-ship-4core --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=/pref/Pythia/config/coop_pythia.ini --dram_io_freq=2400 --knob_cloudsuite=true -traces /pref/Pythia/CASSANDRA/traces/cassandra_phase3_core0.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase3_core1.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase3_core2.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase3_core3.trace.xz > cassandra_phase3_4T_coop_pythia.out 2>&1
/pref/Pythia/bin/perceptron-multi-coop_pythia-no-ship-4core --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=/pref/Pythia/config/coop_pythia.ini --dram_io_freq=2400 --knob_cloudsuite=true -traces /pref/Pythia/CASSANDRA/traces/cassandra_phase4_core0.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase4_core1.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase4_core2.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase4_core3.trace.xz > cassandra_phase4_4T_coop_pythia.out 2>&1
/pref/Pythia/bin/perceptron-multi-coop_pythia-no-ship-4core --warmup_instructions=50000000 --simulation_instructions=150000000 --l2c_prefetcher_types=coop_pythia --config=/pref/Pythia/config/coop_pythia.ini --dram_io_freq=2400 --knob_cloudsuite=true -traces /pref/Pythia/CASSANDRA/traces/cassandra_phase5_core0.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase5_core1.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase5_core2.trace.xz /pref/Pythia/CASSANDRA/traces/cassandra_phase5_core3.trace.xz > cassandra_phase5_4T_coop_pythia.out 2>&1
