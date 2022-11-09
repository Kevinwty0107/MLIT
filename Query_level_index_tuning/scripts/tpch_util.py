# TODO this should be absorbed into other tpch_util

import os

TPCH_DIR='../tpch-tool' 
TPCH_TOOL_DIR = os.path.join(TPCH_DIR, 'dbgen')
DATA_DIR = '/tmp/tables'
DSN = "dbname=postgres user=wangtaiyi"
TPCH_DSN = "dbname=tpch user=wangtaiyi"

if __name__ ==  "__main__":
    print(os.path.exists(TPCH_DIR))