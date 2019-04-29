#Test LFU command
#QUESTION: Should I be overwriting the frequency of every address
#every time a swap is made?? Should I keep a running total of
#it's frequency even from before the swap??

import sys, os

def lfu(processes, ph_mem_size):
    #Make a second dictionary the size of processes to hold frequency count
    frequencies = {}
    for i in range(len(processes)):
        frequencies[i] = 0

    page_table = {}
    page_faults = 0

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

            #If not, use the algorithm to replace LFU element
            else:
                #Find the value in the page table with the smallest frequency
                least_frequent = frequencies[0]

                for i in range(len(page_table)):
                    if (frequencies[i] < least_frequent):
                        least_frequent = frequencies[i]

            #Add the item to the page table. 
                page_table[least_frequent] = process

            #Increment the fault counter  
            page_faults += 1

        #Increment the frequency counter
        for key, value in page_table.items():
            if value == process:
                frequencies[key] += 1

    return(page_faults)


