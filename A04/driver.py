#!/usr/bin/env python

import requests
import cmd_pkg

#Get the input files from the website, data will be a list
r = requests.get('http://cs.mwsu.edu/~griffin/os_data_files/snapshots/sim_37_5_4096_1024.dat')
data = r.text.split(' ')

#Convert the list to a dictionary and fill with an index key 
processes = {}
index = 0
for item in data:
    processes[index] = item
    index += 1

ph_mem_size = 1024

#Run the data with each scheduling algorithm and count the page faults
fifo_PF = cmd_pkg.fifo(processes, ph_mem_size)
rand_PF = cmd_pkg.rand(processes, ph_mem_size)
lfu_PF = cmd_pkg.lfu(processes, ph_mem_size)
lru_PF = cmd_pkg.lru(processes, ph_mem_size)

print(fifo_PF)
print(rand_PF)
print(lfu_PF)
print(lru_PF)

#Graph and display the page faults per algorithm
cmd_pkg.bar_graph(fifo_PF, lfu_PF, lru_PF, rand_PF, ph_mem_size)

