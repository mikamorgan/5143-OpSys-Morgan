import matplotlib.pyplot as plt

def bar_graph(fpf, lfpf, lrpf, rpf, ph_mem_size):
    #X vaules should be the algorithm names
    x = ['FIFO', 'LFU', 'LRU', 'Random']

    #Will need to make these values the resuts of the different
    #algorithm calls (should be the number of page faults)
    y = [fpf, lfpf, lrpf, rpf]

    plt.bar(x, y)
    plt.title("Page Fault Counts by Scheduling Algorithm " + str(ph_mem_size))

    plt.legend()
    plt.show()