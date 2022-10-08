set -x

HSJ=/opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar

hdfs dfs -rm -r -skipTrash out_dir

yarn jar $HSJ \
        -file "mapper.py" -mapper "mapper.py" \
        -file "reducer.py" -reducer "reducer.py" \
        -numReduceTasks 1 \
        -input  prices\
        -output out_dir
\