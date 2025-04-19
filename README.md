# Group 10: Cooperative Prefetching with Bandwidth-Aware Throttling and Adaptive RL for Multicore Systems

## Overview

This project presents a novel extension to the Pythia framework by introducing a reinforcement learning (RL)-based cooperative prefetching system with multicore awareness and bandwidth-aware throttling. Our work aims to improve memory-level parallelism and reduce cache miss penalties across various benchmark workloads: **Streaming**, **Cloud9**, **Nutch**, and **Cassandra**.

We implemented `CoopPythia`, a new prefetching engine, that adaptively tunes aggressiveness and learns cooperative policies in multicore scenarios. The results demonstrate significant improvements in Instructions Per Cycle (IPC) and controlled overprediction rates.

## Benchmark Descriptions

### Streaming

The Streaming benchmark represents data-intensive applications that rely heavily on sequential memory access patterns. These applications benefit greatly from stride-based and accurate stream prefetchers. In our study, Streaming showed susceptibility to bandwidth saturation under aggressive prefetching, making it an ideal candidate to evaluate bandwidth-aware throttling. Our RL approach was able to identify optimal levels of prefetch aggressiveness and improve accuracy by filtering redundant streams.

Prefetching strategies applied to Streaming highlight the trade-off between coverage and overprediction. The CoopPythia prefetcher reduced overprediction by up to **40%** compared to Scooby, while maintaining high coverage. These results demonstrate that intelligent throttling coupled with cooperative filtering can yield measurable performance gains.

### Cloud9

Cloud9 is characterized by a mix of compute and memory-bound operations commonly found in cloud-scale web services. Its irregular memory access patterns pose a challenge for traditional stride or stream prefetchers. Our cooperative RL engine dynamically adjusted prefetching decisions based on MSHR and memory queue pressure, leading to notable improvements in cache efficiency.

The benchmark showed that multicore collaboration in prefetching significantly reduces redundant accesses across shared LLCs. With CoopPythia, the IPC improved by **13%** over the default Pythia setup, and bandwidth utilization remained below 80%, preventing performance degradation due to prefetch congestion.

### Nutch

Apache Nutch, an open-source web crawler, demonstrates semi-regular memory access behavior with bursts of sequential access during data parsing and random accesses during link graph analysis. The benchmark is memory-bound but difficult to optimize due to its mixed access behavior. Traditional prefetchers either underfetch or flood the cache with irrelevant data.

Our adaptive learning rate mechanism within CoopPythia proved especially beneficial for Nutch. The RL engine was able to gradually learn distinct patterns per phase, reducing useless prefetches by **27%** while sustaining useful prefetch coverage. The results validate the importance of adaptability in RL-based prefetching for heterogeneous workloads.

### Cassandra

Apache Cassandra, a distributed NoSQL database, is a complex benchmark that includes multithreaded read/write workloads, often simulating real-time analytics environments. The access patterns in Cassandra are highly irregular and suffer from inter-core prefetch contention, leading to inefficient bandwidth usage and cache pollution.

By applying a bandwidth-aware filter and recent-prefetch tracking in CoopPythia, we significantly reduced cache pollution and improved IPC by **19%** on average. The cooperative mechanism allowed each core to share confidence levels about address predictions, resulting in smarter global decision-making and lower LLC contention.

## Final Results

| Benchmark  | IPC Improvement (vs Scooby) | Overprediction Reduction |
|------------|-----------------------------|--------------------------|
| Streaming  | +10%                        | -40%                     |
| Cloud9     | +13%                        | -32%                     |
| Nutch      | +11%                        | -27%                     |
| Cassandra  | +19%                        | -35%                     |

The results show CoopPythia consistently outperforms traditional Pythia and Scooby prefetchers in multicore environments, striking a balance between aggressiveness and bandwidth sensitivity.

## Features

- RL-based dynamic prefetching with Q-learning
- Bandwidth-aware throttling to prevent overfetch
- Multicore coordination via shared confidence scores
- Adaptive learning rates based on IPC trends
- Recent-prefetch filters to avoid redundancy

## Repository Structure


