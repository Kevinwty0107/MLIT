#!/bin/bash
# run full
#

# run from Query_level_index_tuning/root
if [ "$(basename $(pwd))" != "Query_level_index_tuning" ]
then 
    echo "start script from Query_level_index_tuning root" ;
    exit ;
fi


echo "#### RUNNING ON EXP CONFIG 0 ####" ;
sh ./scripts/run_experiments.sh
#
# run dqn
#
echo "#### RUNNING ON EXP CONFIG 1####" ;
sh ./scripts/run_experiments_1.sh
#
# run spg
#
#echo "#### RUNNING ON EXP CONFIG 2 ####" ;
#sh ./scripts/run_experiments_2.sh