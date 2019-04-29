#Test FIFO command
import sys, os

def fifo(processes, ph_mem_size):
    page_table = {}

    #FIFO Implementation
    page_faults = 0

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

        #Add the item to the page table. 
        #Use the modulus operator to loop around the size of the page table
        #every time an element needs to be replaced (FIFO method)
            page_table[(page_faults % ph_mem_size)] = process

    return(page_faults)


