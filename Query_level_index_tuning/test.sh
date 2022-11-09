# run from rlautoindex/root
# run from rlautoindex/root
if [ "$(basename $(pwd))" != "Query_level_index_tuning" ]
then 
    echo "start script from Query_level_index_tuning root" ;
    exit ;
fi

RESULT_DIR=../res/ 
mkdir ${RESULT_DIR}
RESULT_DIR=${RESULT_DIR}$(date '+%m-%d-%y_%H:%M')
mkdir ${RESULT_DIR}