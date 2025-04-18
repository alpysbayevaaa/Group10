import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np

def calculate_full_components(files, level_prefix):
    data = []
    miss_suffix = "LLC_total_miss" if level_prefix == "LLC" else "L2C_total_miss"

    for file in files:
        df = pd.read_csv(file)
        benchmark = file.split("rollup-")[1].split("-core")[0]

        for core in range(4):
            useful_col = f"Core_{core}_{level_prefix}_prefetch_useful"
            useless_col = f"Core_{core}_{level_prefix}_prefetch_useless"
            miss_col = f"Core_{core}_{miss_suffix}"

            if all(col in df.columns for col in [useful_col, useless_col, miss_col]):
                useful = df[useful_col].replace([np.inf, -np.inf], 0).fillna(0)
                useless = df[useless_col].replace([np.inf, -np.inf], 0).fillna(0)
                total_miss = df[miss_col].replace([np.inf, -np.inf], 0).fillna(0)
                exp = df["Exp"]

                for e, u, us, tm in zip(exp, useful, useless, total_miss):
                    uncovered = max(0, tm - u)
                    data.append({
                        "Benchmark": benchmark,
                        "Exp": e,
                        "Core": core,
                        "Covered": u,
                        "Overpredicted": us,
                        "Uncovered": uncovered,
                        "Level": level_prefix
                    })
    return pd.DataFrame(data)

def plot_stacked_chart(df, title):
    experiments = df["Exp"].unique()
    core_labels = [f"Core {i}" for i in range(4)]

    bar_width = 0.15
    core_gap = 0.05
    group_gap = 0.6

    bar_positions = []
    x = 0
    for _ in experiments:
        core_positions = [x + i * (bar_width + core_gap) for i in range(4)]
        bar_positions.append(core_positions)
        x = core_positions[-1] + bar_width + group_gap

    avg_start = x
    avg_positions = [avg_start + i * (bar_width + core_gap) for i in range(len(experiments))]
    group_labels_pos = [np.mean(pos) for pos in bar_positions]
    avg_label_pos = np.mean(avg_positions)

    fig, ax = plt.subplots(figsize=(22, 10))

    for i, exp in enumerate(experiments):
        sub_df = df[df["Exp"] == exp].groupby("Core")[["Covered", "Overpredicted", "Uncovered"]].mean()
        xpos = bar_positions[i]

        btm = np.zeros(len(sub_df))
        ax.bar(xpos, sub_df["Covered"], width=bar_width, color='black')
        btm += sub_df["Covered"].values
        ax.bar(xpos, sub_df["Overpredicted"], bottom=btm, width=bar_width, color='gray')
        btm += sub_df["Overpredicted"].values
        ax.bar(xpos, sub_df["Uncovered"], bottom=btm, width=bar_width, color='lightgray')

        for j, x_val in enumerate(xpos):
            ax.text(x_val, -0.02, core_labels[j], ha='center', va='top', fontsize=18, rotation=90)

        ax.text(group_labels_pos[i], btm.max() + sub_df["Uncovered"].values.max() + 0.05, exp,
                ha='center', va='bottom', fontsize=20, fontweight='bold')

    for i, exp in enumerate(experiments):
        values = df[df["Exp"] == exp][["Covered", "Overpredicted", "Uncovered"]]
        c_avg = values["Covered"].mean()
        o_avg = values["Overpredicted"].mean()
        u_avg = values["Uncovered"].mean()
        xpos = avg_positions[i]

        ax.bar(xpos, c_avg, width=bar_width, color='black')
        ax.bar(xpos, o_avg, bottom=c_avg, width=bar_width, color='gray')
        ax.bar(xpos, u_avg, bottom=c_avg + o_avg, width=bar_width, color='lightgray')
        ax.text(xpos, -0.02, exp, ha='center', va='top', fontsize=20, rotation=90)

    max_val = df[["Covered", "Overpredicted", "Uncovered"]].sum(axis=1).max()
    ax.text(avg_label_pos, max_val*0.6, "AVG", ha='center', va='bottom', fontsize=20, fontweight='bold')
    ax.set_ylabel(f'{title} Coverage Breakdown', fontsize=25)
    ax.set_title(f'{title} Prefetch Breakdown: Covered + Overpredicted + Uncovered', fontsize=30)
    ax.set_ylim(0, max_val + 0.02)
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticks([])
    ax.grid(axis='y', linestyle='--', linewidth=0.5)
    ax.legend(['Covered', 'Overpredicted', 'Uncovered'], fontsize=18)
    plt.tight_layout()
    plt.show()

# === RUN ===
files = glob.glob("rollup-*-core.csv")  # adjust path if needed
llc_df = calculate_full_components(files, "LLC")
l2c_df = calculate_full_components(files, "L2C")

plot_stacked_chart(llc_df, "LLC")
plot_stacked_chart(l2c_df, "L2C")

