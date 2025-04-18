#include "coop_pythia.h"
#include <iostream>
#include "knobs.h"

using namespace std;

CoopPythiaPrefetcher::CoopPythiaPrefetcher(std::string type)
    : Prefetcher(type), learning_alpha(0.1), current_bw_level(0), current_ipc(0), current_acc(0), pf_useful(0)
{
}

void CoopPythiaPrefetcher::invoke_prefetcher(uint64_t ip, uint64_t addr, uint8_t cache_hit, uint8_t type, std::vector<uint64_t> &pf_addrs)
{
    if (!knob::coop_enable_bw_throttling || bandwidth_ok()) {
        if (knob::coop_enable_multicore)
            perform_multicore_prefetching(ip, addr, pf_addrs);
        else
            perform_local_prefetching(ip, addr, pf_addrs);
    }
}

void CoopPythiaPrefetcher::perform_local_prefetching(uint64_t ip, uint64_t addr, std::vector<uint64_t> &pf_addrs)
{
    const int max_pf_per_cycle = 2;
    uint64_t pf_addr = addr + 64;
    if (should_issue_prefetch(pf_addr) && pf_addrs.size() < max_pf_per_cycle)
        pf_addrs.push_back(pf_addr);
}

void CoopPythiaPrefetcher::perform_multicore_prefetching(uint64_t ip, uint64_t addr, std::vector<uint64_t> &pf_addrs)
{
    const int max_pf_per_cycle = 2;
    uint64_t pf_addr1 = addr + 64;
    uint64_t pf_addr2 = addr + 128;

    if (should_issue_prefetch(pf_addr1) && pf_addrs.size() < max_pf_per_cycle)
        pf_addrs.push_back(pf_addr1);
    if (should_issue_prefetch(pf_addr2) && pf_addrs.size() < max_pf_per_cycle)
        pf_addrs.push_back(pf_addr2);
}

void CoopPythiaPrefetcher::register_fill(uint64_t addr)
{
    fill_history.insert(addr);
}

void CoopPythiaPrefetcher::register_prefetch_hit(uint64_t addr)
{
    if (fill_history.find(addr) != fill_history.end()) {
        pf_useful++;
    }
}

void CoopPythiaPrefetcher::update_bw(uint8_t bw_level)
{
    current_bw_level = bw_level;
}

void CoopPythiaPrefetcher::update_ipc(uint8_t ipc)
{
    current_ipc = ipc;

    if (knob::coop_enable_adaptive_alpha) {
        if (ipc > knob::coop_rl_ipc_threshold)
            learning_alpha = knob::coop_rl_alpha_high_ipc;
        else
            learning_alpha = knob::coop_rl_alpha_low_ipc;
    }
}

void CoopPythiaPrefetcher::update_acc(uint8_t acc_level)
{
    current_acc = acc_level;
}

bool CoopPythiaPrefetcher::bandwidth_ok()
{
    if (!linked_cache) return true;

    return linked_cache->MSHR.occupancy < (linked_cache->MSHR_SIZE * 0.5) &&
           linked_cache->PQ.occupancy   < (linked_cache->PQ_SIZE   * 0.5);
}

bool CoopPythiaPrefetcher::should_issue_prefetch(uint64_t addr)
{
    if (!linked_cache) return true;

    if (linked_cache->check_mshr_hit(addr)) return false;
    if (linked_cache->check_pq_hit(addr)) return false;

    return true;
}

void CoopPythiaPrefetcher::dump_stats()
{
    cout << "[CoopPythia Stats]" << endl;
    cout << " - Useful prefetches: " << pf_useful << endl;
    cout << " - Final alpha: " << learning_alpha << endl;
}

void CoopPythiaPrefetcher::print_config()
{
    cout << "[CoopPythia Config]" << endl;
    cout << " - Bandwidth-aware throttling: " << (knob::coop_enable_bw_throttling ? "Enabled" : "Disabled") << endl;
    cout << " - Multicore cooperation: " << (knob::coop_enable_multicore ? "Enabled" : "Disabled") << endl;
    cout << " - RL Enabled: " << (knob::coop_rl_enable ? "Yes" : "No") << endl;
    cout << " - Adaptive Alpha: " << (knob::coop_enable_adaptive_alpha ? "Enabled" : "Disabled") << endl;
    cout << " - IPC Threshold: " << static_cast<int>(knob::coop_rl_ipc_threshold) << endl;
    cout << " - BW Threshold: " << static_cast<int>(knob::coop_rl_bw_threshold) << endl;
    cout << " - Alpha High: " << knob::coop_rl_alpha_high_ipc << endl;
    cout << " - Alpha Low: " << knob::coop_rl_alpha_low_ipc << endl;
}
