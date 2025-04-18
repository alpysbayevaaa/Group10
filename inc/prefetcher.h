#ifndef PREFETCHER_H
#define PREFETCHER_H

#include <string>
#include <vector>
#include <cstdint>

class Prefetcher
{
protected:
	std::string type;

public:
	Prefetcher(std::string _type) { type = _type; }
	virtual ~Prefetcher() {}

	std::string get_type() { return type; }

	virtual void invoke_prefetcher(uint64_t pc, uint64_t address, uint8_t cache_hit, uint8_t type, std::vector<uint64_t>& pref_addr) = 0;
	virtual void dump_stats() = 0;
	virtual void print_config() = 0;

	// ➕ Add virtual hooks for optional prefetcher extensions
	virtual void register_fill(uint64_t addr) {}
	virtual void register_prefetch_hit(uint64_t addr) {}
	virtual void update_bw(uint8_t bw_level) {}
	virtual void update_ipc(uint8_t ipc) {}
	virtual void update_acc(uint8_t acc_level) {}
};

#endif /* PREFETCHER_H */
