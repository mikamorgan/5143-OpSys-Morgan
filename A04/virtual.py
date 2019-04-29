import sys, os
import requests

r = requests.get('http://cs.mwsu.edu/~griffin/vm_snapshots/sim_0_3_128.dat')

data = r.text.split(' ')

for item in data:
    p,add = item.split(',')
    
    print("p:{} , add:{}".format(p,add))

def str_binary(n,padd=12):
    binfrmt = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=padd, type='b')
    n = format(n,binfrmt)
    return n

def myargs(sysargs):
    args = {}

    for val in sysargs[1:]:
        k,v = val.split('=')
        args[k] = v
    return args

def read_file(fin,delimiter="\n"):
    if os.path.isfile(fin):
        with open(fin) as f:
            data = f.read()
        data = data.strip()
        return data.split(delimiter)
    return None

if __name__=='__main__':
    args = myargs(sys.argv)

    data = read_file(args['filename']," ")

    for d in data:
        p,h = d.split(',')
        n = int(h, 16)
        b = str_binary(n,5)

        print("{} {} {} {}".format(p,h,n,b))

