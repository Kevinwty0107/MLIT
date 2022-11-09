import pickle
import psqlparse
from Preprocess import Dataset as ds
from Utility import Encoding as en
from Utility import ParserForIndex as pi
import numpy as np

enc = en.encoding_schema()
# path to your tpch_directory/dbgen
work_dir = "../tpch-tool/dbgen"
w_size = 14
wd_generator = ds.TPCH(work_dir, w_size)
workload = wd_generator.gen_workloads()

parser = pi.Parser(enc['attr'])

def preprocess_workload(wd):
    
    with open("wl.txt",'w') as f:
        f.write(wd)
    data = ""
    with open('wl.txt', 'rt') as f:
        a = [x for x in f.readlines()]
    with open('wl.txt', 'rt') as f:
        i = 0
        for line in f.readlines():
            if 0 < i<len(a)-1:
                data = data + line
            i+=1

    return data


def gen_i(__x, workload):
    added_k = set()
    for i in range(len(workload)):
        workload[i] = preprocess_workload(workload[i])
    with open('wl.pickle', 'wb') as df:
        pickle.dump(workload, df, protocol=0)

    wf1 = open('wl.pickle', 'rb')
    workload = pickle.load(wf1)
    wf1.close()
    for k in range(len(workload)):
        if k > __x:
            continue
        b = psqlparse.parse_dict(workload[k])
        parser.parse_stmt(b[0])
        parser.gain_candidates()
        if k == 8:
            added_k.add('lineitem#l_shipmode')
            added_k.add('lineitem#l_orderkey,l_shipmode')
            added_k.add('lineitem#l_shipmode,l_orderkey')
    f_k = parser.index_candidates | added_k
    f_k = list(f_k)
    f_k.sort()
    with open('cands'+str(__x+1)+'.pickle', 'wb') as df:
        pickle.dump(list(f_k), df, protocol=0)


gen_i(14,workload)