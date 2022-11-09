cd /scripts

chmod u+x ... # as appropriate

# install db, db client, and db client driver + db superuser
./setup-db.sh setup -u $(whoami) 

# retrieves and builds tpch tools dbgen and qgen
./build-tpch-tool.sh 

# build tpch database with ~.25 gb of data
# n.b. data is streamed into database by buffering through /tmp, so attn to disk space in particular on root partition
./tpch.py -r -s .25 

# may need to move the default data_directory, depending on desired scale factor
# https://www.digitalocean.com/community/tutorials/how-to-move-a-postgresql-data-directory-to-a-new-location-on-ubuntu-16-04
