#Test LRU command
import sys, os

def lru(processes, ph_mem_size):

    #Make a second dictionary the size of physical memory to hold the iteration count
    iteration = {}
    for x in range(ph_mem_size):
        iteration[x] = 0

    page_table = {}
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

        if (flag):
            #If there is an empty spot in the page table, fill it
            if (len(page_table) < ph_mem_size):
                page_table[page_faults] = process

            #If not, use the algorithm to replace LRU element
            else:
                #Find the value in the page table that was used the longest ago
                least_recent = iteration[0]

                for j in range(ph_mem_size):
                    if (iteration[j] < least_recent):
                        least_recent = iteration[j]

            #Add the item to the page table. 
                for key, value in iteration.items():
                    if value == least_recent:
                        page_table[key] = process

            #Increment the fault counter  
            page_faults += 1

        #Update the frequency counter
        for key, value in page_table.items():
            if value == process:
                iteration[key] = i

    return(page_faults)



