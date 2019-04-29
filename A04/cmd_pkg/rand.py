#Test random command
import sys, os
import random

def rand(processes, ph_mem_size):
    page_table = {}

    #Random Implementation
    page_faults = 0

    #Setup with practice page table size of five
    for i in range(len(processes)):
        #Get the process
        process = processes.get(i)
        flag = True

        #See if it is already in the page table
        for key, value in page_table.items():
            if value == process:
                flag = False

        #If it is not, increment the fault counter     
        if (flag):
            page_faults += 1

        #If there is an empty spot in the page table, fill it
            if (len(page_table) < ph_mem_size):
                page_table[page_faults] = process

            #If not, randomly replace an element
            else:
                page_table[random.randint(0,len(page_table))] = process

    return(page_faults)


