import numpy as np
import pickle
import Model.DQN as model
import Utility.PostgreSQL as pg


def One_Run_DQN(conf, __x, a):
    conf['NAME'] = 'MA_9' + str(__x)
    print('=====load workload=====')
    wf = open('data/workload.pickle', 'rb')
    workload = pickle.load(wf)
    wf.close()
    print('=====load candidate =====')
    cf = open('data/cands.pickle', 'rb')
    index_candidates = pickle.load(cf)
    cf.close()


    agent = model.DQN(workload, index_candidates, 'hypo', conf)
    _indexes, storages = agent.train(False, __x)
    indexes = []
    for _i, _idx in enumerate(_indexes):
        if _idx == 1.0:
            indexes.append(index_candidates[_i])
    return indexes


def get_performance(f_indexes, _frequencies):
    # _frequencies = [1659, 1301, 1190, 1741, 1688, 1242, 1999, 1808, 1433, 1083, 1796, 1266, 1046, 1353]
    frequencies = np.array(_frequencies) / np.array(_frequencies).sum()
    wf = open('workload.pickle', 'rb')
    workload = pickle.load(wf)
    pg_client = pg.PGHypo()
    pg_client.delete_indexes()
    cost1 = (np.array(pg_client.get_queries_cost(workload))*frequencies).sum()
    print(cost1)
    for f_index in f_indexes:
        pg_client.execute_create_hypo(f_index)
    cost2 = (np.array(pg_client.get_queries_cost(workload))*frequencies).sum()
    print(cost2)
    pg_client.delete_indexes()
    print((cost1-cost2)/cost1)


conf21 = {'LR': 0.002, 'EPISILO': 0.97, 'Q_ITERATION': 200, 'U_ITERATION': 5, 'BATCH_SIZE': 64, 'GAMMA': 0.95,
          'EPISODES': 800, 'LEARNING_START': 1000, 'MEMORY_CAPACITY': 20000}

conf = {'LR': 0.1, 'EPISILO': 0.9, 'Q_ITERATION': 9, 'U_ITERATION': 3, 'BATCH_SIZE': 8, 'GAMMA': 0.9,
        'EPISODES': 800, 'LEARNING_START': 400, 'MEMORY_CAPACITY': 800}


# is_fixcount == True, constraint is the index number
# is_fixcount == False, constraint is the index storage unit
def entry(constraint):

    print(One_Run_DQN(conf, constraint, 0))


if __name__ == "__main__":

    entry(4)