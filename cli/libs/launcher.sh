PWD=$(pwd)
java_args=$(cat $PWD/libs/launch-args.txt)

java $java_args
