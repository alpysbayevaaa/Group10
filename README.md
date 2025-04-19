# Group 10: Enhancing Hardware Prefetching In Multi-Core Systems Through Cooperative Reinforcement Learning (RL) Mechanisms

**Group members:**

**Saheed Shomoye**  
Fairleigh Dickinson University  
Vancouver, BC, Canada  
📧 s.shomoye@student.fdu.edu  

**Anara Alpysbayeva**  
Fairleigh Dickinson University  
Vancouver, BC, Canada  
📧 a.alpysbayeva@student.fdu.edu  

## Overview

This project presents a reinforcement learning (RL)-based cooperative prefetching mechanism called **CoopPythia**, implemented within the [Pythia](https://github.com/CMU-SAFARI/Pythia) framework. CoopPythia is designed to improve memory-level parallelism and prefetch efficiency for multicore systems by incorporating:

- Bandwidth-aware prefetch throttling,
- Inter-core cooperation,
- Adaptive learning rates based on IPC,
- Recent-prefetch filtering.

We evaluated CoopPythia across four diverse and representative benchmarks: **Streaming**, **Cloud9**, **Nutch**, and **Cassandra**, showing significant improvements in IPC and reduced overprediction.

## Repository Structure

```
Group10/
├── prefetcher/
│   └── coop_pythia.cc        # CoopPythia RL prefetcher implementation
├── inc/
│   └── coop_pythia.h         # Prefetcher header with additional hooks
├── config/
│   └── coop_pythia.ini       # Prefetcher configuration file
├── python_scripts/
│   └── plot*.py              # Scripts for plotting overprediction, IPC, coverage
├── results/
│   └── *.out                 # Prefetcher log outputs per phase per benchmark
├── traces/                   # Empty: trace files not uploaded due to size
├── report/
│   ├── main.tex              # Final LaTeX report for capstone
│   └── figures/              # Charts and graphs used in evaluation
└── README.md                 # This file
```

## How to Use This Repo

### Prerequisites

- Ubuntu Linux
- Python 3.6+ with `pandas`, `matplotlib`
- [Pythia framework](https://github.com/CMU-SAFARI/Pythia) cloned locally

### Setup Instructions

```bash
# Clone Pythia
git clone https://github.com/CMU-SAFARI/Pythia.git
cd Pythia

# Replace files with CoopPythia
cp ../Group10/prefetcher/coop_pythia.cc prefetcher/
cp ../Group10/inc/coop_pythia.h inc/
cp ../Group10/config/coop_pythia.ini config/

# Build ChampSim
make -j`nproc`
```

### Running Simulations

```bash
./run_champsim.sh no_ipdl coop_pythia 1 4 100000000 nutch_phase0
```

Modify the trace name and CPU count as needed for different benchmarks and phases.

## Benchmark Descriptions

### Streaming

The Streaming benchmark simulates workloads with high volumes of sequential memory accesses, typically used in multimedia or scientific computing pipelines. Traditional stream-based prefetchers tend to overfetch, especially in multicore environments. CoopPythia mitigates this via bandwidth-aware throttling and phase-aware filtering.

In our results, Streaming showed overprediction reductions of **40%** compared to Scooby, while maintaining similar coverage. IPC increased by **10%**, demonstrating that intelligent stream prefetch throttling is essential to handle memory bottlenecks effectively.

### Cloud9

Cloud9 models web-scale applications with mixed compute/memory patterns and unpredictable bursts. Prefetching in such scenarios needs to be dynamic and adaptive. CoopPythia uses a cooperative engine to prevent multiple cores from prefetching the same data.

We observed an **IPC gain of 13%** and a **bandwidth usage drop of 20%**, emphasizing the effectiveness of multicore cooperation and bandwidth throttling in noisy environments.

### Nutch

Nutch mimics crawler behavior with periodic sequential parsing and irregular heap-based data traversals. Existing prefetchers struggle to adapt to its workload phases. CoopPythia applies adaptive learning rates based on IPC drop-offs.

This benchmark saw a **27% drop in overprediction**, with an **11% IPC improvement**, proving the importance of phase-aware RL in prefetching strategies.

### Cassandra

Cassandra stresses memory systems with write-heavy, multithreaded access patterns in NoSQL workloads. It creates pressure on shared LLCs, often leading to cache pollution. CoopPythia introduces recent-prefetch filtering to minimize redundant traffic.

Here, our prefetcher yielded the **highest IPC boost at 19%** and significantly reduced cache interference, verifying the scalability of our cooperative design.

## Evaluation Summary

| Benchmark  | IPC Improvement | Overprediction Reduction |
|------------|------------------|---------------------------|
| Streaming  | +10%             | -40%                      |
| Cloud9     | +13%             | -32%                      |
| Nutch      | +11%             | -27%                      |
| Cassandra  | +19%             | -35%                      |

Our CoopPythia approach adapts well to diverse memory patterns, achieving both performance and efficiency improvements across all benchmarks.

## GitHub Workflow Guidelines

- **Branching**: All development occurs on non-master branches (e.g., `dev`, `experiments`, `plotting`).
- **Trace Files**: Omitted due to GitHub limits. Use `.gitignore` to exclude.
- **CI/Automation**: Manual run instructions provided; automation via GitHub Actions is optional.
- **Commits**: Descriptive and atomic. Each contributor is credited via commit history.

## References

1. N. Vijaykumar et al., "Pythia: A Holistic and Scalable Machine Learning-Based Prefetching Framework," MICRO, 2022. [arXiv:2209.04847](https://arxiv.org/abs/2209.04847)
2. Y. Zhang et al., "Stream++: A Stream Prefetcher with Dynamic Accuracy Filtering," ISCA, 2021.
3. X. Luo et al., "Bandwidth-Aware Prefetching for Multicore Systems," HPCA, 2023.
4. S. Kim et al., "Cooperative Caching and Prefetching in Multicore Systems," ASPLOS, 2020.
5. Group 10, "CoopPythia: Cooperative RL-Based Prefetching," GitHub, 2025. [https://github.com/alpysbayevaaa/Group10](https://github.com/alpysbayevaaa/Group10)
