import numpy as np
import matplotlib.pyplot as plt

# Sample data: (Covered, Uncovered, Overpredicted) per core
data = {
    'SPP': [
        (30, 40, 30),
        (32, 38, 30),
        (31, 39, 30),
        (30, 40, 30)
    ],
    'Bingo': [
        (40, 35, 25),
        (41, 34, 25),
        (39, 36, 25),
        (40, 35, 25)
    ],
    'MLOP': [
        (35, 40, 80),
        (36, 39, 85),
        (34, 41, 90),
        (35, 40, 95)
    ],
    'Pythia': [
        (28, 42, 30),
        (29, 41, 30),
        (27, 43, 30),
        (28, 42, 30)
    ],
    'Coop_Pythia': [
        (33, 40, 40),
        (34, 39, 42),
        (32, 41, 38),
        (33, 40, 40)
    ]
}

prefetchers = list(data.keys())
core_labels = ['Core 0', 'Core 1', 'Core 2', 'Core 3']
n_cores = 4

bar_width = 0.15
core_gap = 0.05
group_gap = 0.6

# Compute X positions
bar_positions = []
x = 0
for _ in prefetchers:
    core_positions = [x + i * (bar_width + core_gap) for i in range(n_cores)]
    bar_positions.append(core_positions)
    x = core_positions[-1] + bar_width + group_gap

# AVG bars
avg_start = x
avg_positions = [avg_start + i * (bar_width + core_gap) for i in range(len(prefetchers))]

# Group label centers
group_labels_pos = [np.mean(pos) for pos in bar_positions]
avg_label_pos = np.mean(avg_positions)

# Plotting
fig, ax = plt.subplots(figsize=(22, 10))

colors = {
    'covered': 'black',
    'uncovered': 'gray',
    'overpredicted': 'lightgray'
}

# Plot core bars
for i, pf in enumerate(prefetchers):
    covered = [data[pf][j][0] for j in range(n_cores)]
    uncovered = [data[pf][j][1] for j in range(n_cores)]
    overpredicted = [data[pf][j][2] for j in range(n_cores)]

    xpos = bar_positions[i]
    ax.bar(xpos, covered, width=bar_width, color=colors['covered'], label='Covered' if i == 0 else "")
    ax.bar(xpos, uncovered, bottom=covered, width=bar_width, color=colors['uncovered'], label='Uncovered' if i == 0 else "")
    ax.bar(xpos, overpredicted, bottom=np.array(covered) + np.array(uncovered),
           width=bar_width, color=colors['overpredicted'], label='Overpredicted' if i == 0 else "")

    # Core labels under each core bar
    for j, x_val in enumerate(xpos):
        ax.text(
            x_val,
            -10,
            core_labels[j],
            ha='center',
            va='top',
            fontsize=18,
            rotation=90
        )

    # Prefetcher label above the core group
    top_val = max([sum(val) for val in data[pf]]) + 10
    ax.text(
        group_labels_pos[i],
        top_val,
        pf,
        ha='center',
        va='bottom',
        fontsize=20,
        fontweight='bold'
    )

# Plot AVG bars
for i, pf in enumerate(prefetchers):
    values = np.array(data[pf])
    avg_vals = values.mean(axis=0)
    xpos = avg_positions[i]
    ax.bar(xpos, avg_vals[0], width=bar_width, color=colors['covered'])
    ax.bar(xpos, avg_vals[1], bottom=avg_vals[0], width=bar_width, color=colors['uncovered'])
    ax.bar(xpos, avg_vals[2], bottom=avg_vals[0] + avg_vals[1], width=bar_width, color=colors['overpredicted'])

    # Prefetcher label below each AVG bar
    ax.text(
        xpos,
        -10,
        pf,
        ha='center',
        va='top',
        fontsize=18,
        rotation=90
    )

# AVG label above AVG block
avg_top = max([sum(np.array(data[pf]).mean(axis=0)) for pf in prefetchers]) + 10
ax.text(
    avg_label_pos,
    avg_top,
    'AVG',
    ha='center',
    va='bottom',
    fontsize=20,
    fontweight='bold'
)

# Hide x-ticks
ax.set_xticks([])

# Axis formatting
ax.set_ylabel('Fraction of LLC misses (%)', fontsize=25)
ax.set_title('Cloudsuite – Coverage and Overprediction by Core', fontsize=25, pad=20)
ax.tick_params(axis='y', labelsize=25)
ax.set_ylim(0, 250)
ax.legend(fontsize=22)
ax.grid(axis='y', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
