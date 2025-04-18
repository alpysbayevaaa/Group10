#ifndef KNOBS_H
#define KNOBS_H

#include <vector>
#include <cstdint>
#define MAX_LEN 256

#include <string>

namespace knob {
    extern bool coop_enable_bw_throttling;
    extern bool coop_enable_multicore;
    extern bool coop_rl_enable;
    extern uint8_t coop_rl_ipc_threshold;
    extern float coop_rl_alpha_high_ipc;
    extern float coop_rl_alpha_low_ipc;
    extern uint32_t coop_rl_bw_threshold;
    extern bool coop_enable_adaptive_alpha;
}

void parse_args(int argc, char* argv[]);
void parse_config(char *config_file_name);
int parse_knobs(void* user, const char* section, const char* name, const char* value);
int handler(void* user, const char* section, const char* name, const char* value);

/* auxiliary functions */
std::vector<int32_t> get_array_int(const char *str);
std::vector<float> get_array_float(const char *str);



#endif /* KNOBS_H */
