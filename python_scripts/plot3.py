import numpy as np
import matplotlib.pyplot as plt

# Define custom dtype
my_dtype = np.dtype([
    ('Trace', 'U10'),
    ('Exp', 'U20'),
    ('Core_0_IPC', 'f8'), ('Core_1_IPC', 'f8'),
    ('Core_2_IPC', 'f8'), ('Core_3_IPC', 'f8'),
    ('Core_0_LLC_total_miss', 'i8'), ('Core_0_LLC_load_miss', 'i8'),
    ('Core_0_LLC_RFO_miss', 'i8'), ('Core_0_LLC_writeback_miss', 'i8'),
    ('Core_1_LLC_total_miss', 'i8'), ('Core_1_LLC_load_miss', 'i8'),
    ('Core_1_LLC_RFO_miss', 'i8'), ('Core_1_LLC_writeback_miss', 'i8'),
    ('Core_2_LLC_total_miss', 'i8'), ('Core_2_LLC_load_miss', 'i8'),
    ('Core_2_LLC_RFO_miss', 'i8'), ('Core_2_LLC_writeback_miss', 'i8'),
    ('Core_3_LLC_total_miss', 'i8'), ('Core_3_LLC_load_miss', 'i8'),
    ('Core_3_LLC_RFO_miss', 'i8'), ('Core_3_LLC_writeback_miss', 'i8'),
    ('Filter', 'i8')
])

# Load datasets
workload_names = ['cassandra', 'cloud9', 'nutch', 'streaming']
csv_files = [f'rollup-{name}-final.csv' for name in workload_names]
workloads = [np.genfromtxt(file, dtype=my_dtype, delimiter=',', names=True) for file in csv_files]

# Define prefetcher types (experiments)
experiments = ['nopref', 'dspatch', 'mlop', 'bingo', 'ppf', 'pythia', 'coop_pythia', 'spp']

# Initialize IPC matrix
ipc_matrix = np.zeros((len(workload_names), len(experiments)))  # rows: workloads, cols: experiments

# Fill IPC matrix
for w_idx, workload in enumerate(workloads):
    for e_idx, exp in enumerate(experiments):
        mask = workload['Exp'] == exp
        if np.any(mask):
            ipc_sum = (
                workload['Core_0_IPC'][mask].sum() +
                workload['Core_1_IPC'][mask].sum() +
                workload['Core_2_IPC'][mask].sum() +
                workload['Core_3_IPC'][mask].sum()
            )
            ipc_matrix[w_idx, e_idx] = ipc_sum

# Calculate % improvement vs nopref
nopref_ipc = ipc_matrix[:, 0:1]  # shape (N, 1)
improvement_pct = (ipc_matrix - nopref_ipc) / nopref_ipc * 100  # broadcasting

# Plotting
bar_width = 0.10
x = np.arange(len(workload_names))

colors = [
    '#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3',
    '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3'
]
hatches = ['//', '', '', '', '', '', '', '\\']

plt.figure(figsize=(18, 9))

for i, (label, color, hatch) in enumerate(zip(experiments, colors, hatches)):
    bar_positions = x + i * bar_width
    bars = plt.bar(bar_positions, ipc_matrix[:, i], width=bar_width, label=label,
                   color=color, edgecolor='black', hatch=hatch)

    # Add % diff on top of each bar (skip nopref since it's the baseline)
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if i == 0:
            text = "0.00%"
        else:
            delta = improvement_pct[j, i]
            text = f"{delta:+.2f}%"
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.1,
            text,
            ha='center',
            va='bottom',
            fontsize=17,
            rotation=90
        )

# Styling
plt.xticks(x + bar_width * (len(experiments)-1)/2, workload_names, fontsize=25)
plt.yticks(fontsize=25)
plt.xlabel("Benchmarks", fontsize=25)
plt.ylabel("Total IPC (sum of 4 cores)", fontsize=25)
plt.title("Cloud Suite - IPC Comparison (% Diff from NOPREF)", fontsize=30)
plt.ylim(0, np.max(ipc_matrix) + 2)
plt.legend(title="Prefetcher", fontsize=17, title_fontsize=20)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()
