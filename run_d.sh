set -x

HSJ=/opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar

hdfs dfs -rm -r -skipTrash out_dir2

yarn jar $HSJ \
        -file "mapper_d.py" -mapper "mapper_d.py" \
        -file "reducer_d.py" -reducer "reducer_d.py" \
        -numReduceTasks 1 \
        -input  prices\
        -output out_dir2
\