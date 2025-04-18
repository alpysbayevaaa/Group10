#ifndef COOP_PYTHIA_H
#define COOP_PYTHIA_H

#include <unordered_set>
#include <vector>
#include <string>
#include <iostream>
#include "prefetcher.h"
#include "cache.h"

class CoopPythiaPrefetcher : public Prefetcher {
public:
    CoopPythiaPrefetcher(std::string type);

    void invoke_prefetcher(uint64_t ip, uint64_t addr, uint8_t cache_hit, uint8_t type,
                           std::vector<uint64_t> &pf_addrs) override;

    void register_fill(uint64_t addr) override;
    void register_prefetch_hit(uint64_t addr) override;

    void update_bw(uint8_t bw_level) override;
    void update_ipc(uint8_t ipc) override;
    void update_acc(uint8_t acc_level) override;

    void dump_stats() override;
    void print_config() override;

    void link_cache(CACHE* cache);

private:
    float learning_alpha;
    uint8_t current_bw_level;
    uint8_t current_ipc;
    uint8_t current_acc;
    std::unordered_set<uint64_t> fill_history;
    CACHE* linked_cache = nullptr;
    uint64_t pf_useful = 0;

    bool bandwidth_ok();
    bool should_issue_prefetch(uint64_t addr); // 🆕 Deadlock-safe check

    void perform_local_prefetching(uint64_t ip, uint64_t addr,
                                   std::vector<uint64_t> &pf_addrs);

    void perform_multicore_prefetching(uint64_t ip, uint64_t addr,
                                       std::vector<uint64_t> &pf_addrs);
};

#endif // COOP_PYTHIA_H
