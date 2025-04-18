from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

#style.use('ggplot')

my_dtype = np.dtype([
    ('Trace', 'U10'),            # string (up to 10 characters)
    ('Exp', 'U10'),            # string (up to 10 characters)
    ('Core_0_IPC', 'f8'),      # 64-bit float
    ('Core_1_IPC', 'f8'),       # 64-bit float
    ('Core_2_IPC', 'f8'),       # 64-bit float
    ('Core_3_IPC', 'f8'),       # 64-bit float
    ('Core_0_LLC_total_miss', 'i8'),    
    ('Core_0_LLC_load_miss', 'i8'),    
    ('Core_0_LLC_RFO_miss', 'i8'),    
    ('Core_0_LLC_writeback_miss', 'i8'),
    ('Core_1_LLC_total_miss', 'i8'), 
    ('Core_1_LLC_load_miss', 'i8'), 
    ('Core_1_LLC_RFO_miss', 'i8'), 
    ('Core_1_LLC_writeback_miss', 'i8'),
    ('Core_2_LLC_total_miss', 'i8'),   
    ('Core_2_LLC_load_miss', 'i8'),   
    ('Core_2_LLC_RFO_miss', 'i8'),   
    ('Core_2_LLC_writeback_miss', 'i8'),
    ('Core_3_LLC_total_miss', 'i8'),   
    ('Core_3_LLC_load_miss', 'i8'),   
    ('Core_3_LLC_RFO_miss', 'i8'),   
    ('Core_3_LLC_writeback_miss', 'i8'),
    ('Filter', 'i8')   
])

N = 4

cassandra = np.genfromtxt('rollup-cassandra-final.csv', dtype = my_dtype, delimiter = ',', names = True)
cloud9 = np.genfromtxt('rollup-cloud9-final.csv', dtype = my_dtype, delimiter = ',', names = True)
nutch = np.genfromtxt('rollup-nutch-final.csv', dtype = my_dtype, delimiter = ',', names = True)
streaming = np.genfromtxt('rollup-streaming-final.csv', dtype = my_dtype, delimiter = ',', names = True)

print(type(cassandra))

workloads=[cassandra,cloud9,nutch,streaming]
unique_Exp = np.unique(cassandra['Exp'])

"""
Core 0
"""
nopref_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'nopref']) for workload in workloads}
bingo_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'bingo']) for workload in workloads}
dspatch_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'dspatch']) for workload in workloads}
mlop_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'mlop']) for workload in workloads}
ppf_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'ppf']) for workload in workloads}
pythia_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'pythia']) for workload in workloads}
coop_pythia_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'coop_pythia']) for workload in workloads}
spp_sum_0 = {f"{workload=}": np.sum(workload['Core_0_IPC'][workload['Exp'] == 'spp']) for workload in workloads}

"""
Core 1
"""
nopref_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'nopref'].astype(float).sum() for workload in workloads}
bingo_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'bingo'].astype(float).sum() for workload in workloads}
dspatch_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'dspatch'].astype(float).sum() for workload in workloads}
mlop_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'mlop'].astype(float).sum() for workload in workloads}
ppf_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'ppf'].astype(float).sum() for workload in workloads}
pythia_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'pythia'].astype(float).sum() for workload in workloads}
coop_pythia_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'coop_pythia'].astype(float).sum() for workload in workloads}
spp_sum_1 = {f"{workload=}": workload['Core_1_IPC'][workload['Exp'] == 'spp'].astype(float).sum() for workload in workloads}

"""
Core 2
"""
nopref_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'nopref'].astype(float).sum() for workload in workloads}
bingo_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'bingo'].astype(float).sum() for workload in workloads}
dspatch_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'dspatch'].astype(float).sum() for workload in workloads}
mlop_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'mlop'].astype(float).sum() for workload in workloads}
ppf_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'ppf'].astype(float).sum() for workload in workloads}
pythia_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'pythia'].astype(float).sum() for workload in workloads}
coop_pythia_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'coop_pythia'].astype(float).sum() for workload in workloads}
spp_sum_2 = {f"{workload=}": workload['Core_2_IPC'][workload['Exp'] == 'spp'].astype(float).sum() for workload in workloads}

"""
Core 3
"""
nopref_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'nopref'].astype(float).sum() for workload in workloads}
bingo_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'bingo'].astype(float).sum() for workload in workloads}
dspatch_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'dspatch'].astype(float).sum() for workload in workloads}
mlop_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'mlop'].astype(float).sum() for workload in workloads}
ppf_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'ppf'].astype(float).sum() for workload in workloads}
pythia_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'pythia'].astype(float).sum() for workload in workloads}
coop_pythia_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'coop_pythia'].astype(float).sum() for workload in workloads}
spp_sum_3 = {f"{workload=}": workload['Core_3_IPC'][workload['Exp'] == 'spp'].astype(float).sum() for workload in workloads}


"""
Core 0
"""
nopref_x_0 = []
bingo_x_0 = []
dspatch_x_0 = []
mlop_x_0 = []
ppf_x_0 = []
pythia_x_0 = []
coop_pythia_x_0 = []
spp_x_0 = []

"""
Core 1
"""
nopref_x_1 = []
bingo_x_1 = []
dspatch_x_1 = []
mlop_x_1 = []
ppf_x_1 = []
pythia_x_1 = []
coop_pythia_x_1 = []
spp_x_1 = []

"""
Core 2
"""
nopref_x_2 = []
bingo_x_2 = []
dspatch_x_2 = []
mlop_x_2 = []
ppf_x_2 = []
pythia_x_2 = []
coop_pythia_x_2 = []
spp_x_2 = []

"""
Core 3
"""
nopref_x_3 = []
bingo_x_3 = []
dspatch_x_3 = []
mlop_x_3 = []
ppf_x_3 = []
pythia_x_3 = []
coop_pythia_x_3 = []
spp_x_3 = []

"""
Core 0
"""
for workload in workloads:
	nopref_x_0.append(nopref_sum_0[f"{workload=}"])
	bingo_x_0.append(bingo_sum_0[f"{workload=}"])
	dspatch_x_0.append(dspatch_sum_0[f"{workload=}"])
	mlop_x_0.append(mlop_sum_0[f"{workload=}"])
	ppf_x_0.append(ppf_sum_0[f"{workload=}"])
	pythia_x_0.append(pythia_sum_0[f"{workload=}"])
	coop_pythia_x_0.append(pythia_sum_0[f"{workload=}"])
	spp_x_0.append(spp_sum_0[f"{workload=}"])

"""
Core 1
"""
for workload in workloads:
	nopref_x_1.append(nopref_sum_1[f"{workload=}"])
	bingo_x_1.append(bingo_sum_1[f"{workload=}"])
	dspatch_x_1.append(dspatch_sum_1[f"{workload=}"])
	mlop_x_1.append(mlop_sum_1[f"{workload=}"])
	ppf_x_1.append(ppf_sum_1[f"{workload=}"])
	pythia_x_1.append(pythia_sum_1[f"{workload=}"])
	coop_pythia_x_1.append(pythia_sum_1[f"{workload=}"])
	spp_x_1.append(spp_sum_1[f"{workload=}"])

"""
Core 2
"""
for workload in workloads:
	nopref_x_2.append(nopref_sum_2[f"{workload=}"])
	bingo_x_2.append(bingo_sum_2[f"{workload=}"])
	dspatch_x_2.append(dspatch_sum_2[f"{workload=}"])
	mlop_x_2.append(mlop_sum_2[f"{workload=}"])
	ppf_x_2.append(ppf_sum_2[f"{workload=}"])
	pythia_x_2.append(pythia_sum_2[f"{workload=}"])
	coop_pythia_x_2.append(pythia_sum_2[f"{workload=}"])
	spp_x_2.append(spp_sum_2[f"{workload=}"])

"""
Core 3
"""
for workload in workloads:
	nopref_x_3.append(nopref_sum_3[f"{workload=}"])
	bingo_x_3.append(bingo_sum_3[f"{workload=}"])
	dspatch_x_3.append(dspatch_sum_3[f"{workload=}"])
	mlop_x_3.append(mlop_sum_3[f"{workload=}"])
	ppf_x_3.append(ppf_sum_3[f"{workload=}"])
	pythia_x_3.append(pythia_sum_3[f"{workload=}"])
	coop_pythia_x_3.append(pythia_sum_3[f"{workload=}"])
	spp_x_3.append(spp_sum_3[f"{workload=}"])

"""
Declare of sum of Cores
"""
nopref_x = []
bingo_x = []
dspatch_x = []
mlop_x = []
ppf_x = []
pythia_x = []
coop_pythia_x = []
spp_x = []

"""
All Cores 
"""
print(type(nopref_sum_0))
for workload in workloads:
	nopref_x.append(int(nopref_sum_0[f"{workload=}"]) + int(nopref_sum_1[f"{workload=}"]) + int(nopref_sum_2[f"{workload=}"]) + int(nopref_sum_3[f"{workload=}"]))
	bingo_x.append(int(bingo_sum_0[f"{workload=}"]) + int(bingo_sum_1[f"{workload=}"]) + int(bingo_sum_2[f"{workload=}"]) + int(bingo_sum_3[f"{workload=}"]))
	dspatch_x.append(int(dspatch_sum_0[f"{workload=}"]) + int(dspatch_sum_1[f"{workload=}"]) + int(dspatch_sum_2[f"{workload=}"]) + int(dspatch_sum_3[f"{workload=}"]))
	mlop_x.append(int(mlop_sum_0[f"{workload=}"]) + int(mlop_sum_1[f"{workload=}"]) + int(mlop_sum_2[f"{workload=}"]) + int(mlop_sum_3[f"{workload=}"]))
	ppf_x.append(int(ppf_sum_0[f"{workload=}"]) + int(ppf_sum_1[f"{workload=}"]) + int(ppf_sum_2[f"{workload=}"]) + int(ppf_sum_3[f"{workload=}"]))
	pythia_x.append(int(pythia_sum_0[f"{workload=}"]) + int(pythia_sum_1[f"{workload=}"]) + int(pythia_sum_2[f"{workload=}"]) + int(pythia_sum_3[f"{workload=}"]))
	coop_pythia_x.append(int(coop_pythia_sum_0[f"{workload=}"]) + int(coop_pythia_sum_1[f"{workload=}"]) + int(coop_pythia_sum_2[f"{workload=}"]) + int(coop_pythia_sum_3[f"{workload=}"]))
	spp_x.append(int(spp_sum_0[f"{workload=}"]) + int(spp_sum_1[f"{workload=}"]) + int(spp_sum_2[f"{workload=}"]) + int(spp_sum_3[f"{workload=}"]))

for workload in workloads:
	print(nopref_x)

ind = np.arange(0,N,1.25)
width = 0.15
#bar_labels = ['red', 'blue', 'green', 'orange', 'pink']
bar_colors = ['w', 'tab:green', 'tab:blue', 'tab:red', 'tab:grey', 'tab:olive', 'tab:purple', 'w']

fig = plt.subplots(figsize = (15, 8))

p1 = plt.bar(ind, nopref_x, color=bar_colors[0], align='edge', edgecolor='black', width=width, hatch='//')
p2 = plt.bar(ind+3*width/5, dspatch_x, color=bar_colors[1], align='edge', edgecolor='black', width=width)
p3 = plt.bar(ind+6*width/5, mlop_x, color=bar_colors[2], align='edge', edgecolor='black', width=width)
p4 = plt.bar(ind+9*width/5, bingo_x, color=bar_colors[3], align='edge', edgecolor='black', width=width)
p5 = plt.bar(ind+12*width/5, ppf_x, color=bar_colors[4], align='edge', edgecolor='black', width=width)
p6 = plt.bar(ind+15*width/5, pythia_x, color=bar_colors[5], align='edge', edgecolor='black', width=width)
p7 = plt.bar(ind+18*width/5, coop_pythia_x, color=bar_colors[6], align='edge', edgecolor='black', width=width)
p8 = plt.bar(ind+21*width/5, spp_x, color=bar_colors[7], align='edge', edgecolor='black', width=width, hatch='\\')
plt.title('Cloud Suite (MTPS2400)')
plt.xticks(ind+0.55, ("cassandra","cloud9","nutch","streaming"))
plt.ylim(0, 15.0)
plt.xlim(-0.2, 6.7)
plt.legend((p4[0], p2[0], p3[0], p1[0], p5[0], p6[0], p7[0], p8[0]),unique_Exp)
plt.show()
