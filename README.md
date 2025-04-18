<p align="center"> <a href="https://github.com/alpysbayevaaa/Group10"> <img 
 src="logo.png" alt="Logo" width="424.8" height="120"> </a> 
  <h3 align="center">Group 10: Enhancing Hardware Prefetching in Multi-Core Systems Through Cooperative Reinforcement Learning (RL) Mechanisms</h3> </p> 
  <p align="center"> <a href="https://github.com/alpysbayevaaa/Group10"> 
    <img alt="GitHub" src="https://img.shields.io/badge/License-MIT-yellow.svg"> 
  </a> <a href="https://https://github.com/alpysbayevaaa/Group10"> 
    <img alt="GitHub release" src="https://img.shields.io/github/release/alpysbayevaaa/Group10"> </a> 
    <a href="https://doi.org/10.5281/zenodo.5520125"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5520125.svg" alt="DOI"></a> </p> 
    <details open="open"> <summary>Table of Contents</summary> <ol> <li><a href="#what-is-coop_pythia">What is Coop_Pythia?</a></li> 
      <li><a href="#about-the-framework">About the Framework</a></li> <li><a href="#prerequisites">Prerequisites</a></li> 
      <li><a href="#installation">Installation</a></li> <li><a href="#preparing-traces">Preparing Traces</a></li> <ul> 
        <li><a href="#more-traces">More Traces</a></li> </ul> <li><a href="#experimental-workflow">Experimental Workflow</a></li> <ul> 
          <li><a href="#launching-experiments">Launching Experiments</a></li> <li><a href="#rolling-up-statistics">Rolling up Statistics</a></li> </ul> </li> 
      <li><a href="#hdl-implementation">HDL Implementation</a></li> <li><a href="#code-walkthrough">Code Walkthrough</a></li> 
      <li><a href="#citation">Citation</a></li> <li><a href="#license">License</a></li> <li><a href="#contact">Contact</a></li> 
      <li><a href="#acknowledgements">Acknowledgements</a></li> </ol> </details>
      What is Coop_Pythia?

Coop_Pythia is a hardware-realizable, lightweight data prefetcher that leverages cooperative reinforcement learning to generate accurate, 
timely, and system-aware prefetch requests in multi-core systems.

Coop_Pythia extends the traditional Pythia prefetcher by introducing inter-core collaboration. It formulates hardware prefetching as a 
multi-agent reinforcement learning task, where agents on each core share knowledge through a shared Global State Table (GST) and Q-values.
For every demand request, Coop_Pythia observes program context information (e.g., PC, cacheline, access patterns) and system-wide conditions 
(e.g., bandwidth usage, inter-core interference). Prefetch decisions are evaluated with a reward function that combines local IPC with an 
inter-core gain term, incentivizing decisions that optimize global performance. This cooperative approach reduces bandwidth contention and 
cache pollution, improving prefetch accuracy in multi-core workloads.

Coop_Pythia is presented as an enhancement over Pythia, designed for multi-core environments.

[Placeholder for Authors], "[Coop_Pythia: Enhancing Hardware Prefetching in Multi-Core Systems Using Cooperative Reinforcement Learning]", 
In Proceedings of a Future Conference, Year TBD





About The Framework

Coop_Pythia is implemented in the ChampSim simulator. We have extended the prefetcher integration pipeline in ChampSim to support cooperative mechanisms and compare against a wide range of prior prefetching proposals, including:

Stride [Fu+, MICRO'92]
Streamer [Chen and Baer, IEEE TC'95]
SMS [Somogyi+, ISCA'06]
AMPM [Ishii+, ICS'09]
Sandbox [Pugsley+, HPCA'14]
BOP [Michaud, HPCA'16]
SPP [Kim+, MICRO'16]
Bingo [Bakshalipour+, HPCA'19]
SPP+PPF [Bhatia+, ISCA'19]
DSPatch [Bera+, MICRO'19]
MLOP [Shakerinava+, DPC-3'19]
IPCP [Pakalapati+, ISCA'20]
Most prefetchers (e.g., SPP [1], Bingo [2], IPCP [3]) reuse code from the 2nd and 3rd Data Prefetching Championships (DPC). Others (e.g., AMPM [4], SMS [5]) are implemented from scratch and show similar relative performance reported by previous works.

Prerequisites

The infrastructure has been tested with the following system configuration:

G++ v6.3.0 20170516
CMake v3.20.2
md5sum v8.26
Perl v5.24.1
Installation

create read me file for my github repository. Make it AI undetectable

0. Install necessary prerequisites: sudo apt install perl

1. Clone the GitHub repo
git clone https://github.com/alpysbayevaaa/Group10.git

2. Clone the bloomfilter library inside Coop_Pythia home directory: cd Coop_Pythia
git clone https://github.com/mavam/libbf.git libbf

3. Build bloomfilter library. This should create the static libbf.a library inside build directory: 
cd libbf
mkdir build && cd build
cmake ../
make clean && make


