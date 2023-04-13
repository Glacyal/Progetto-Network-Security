pid='%%'
echo $pid
while [ $pid == '%%' ]
 do
 pid=$(ps|grep "python3") #nome del programma
 pid=($pid%% " "*)
 echo "in attesa del pid.."
done
 echo "pid trovato" $pid
 echo $pid
echo "time CPU MEM">file.txt;for i in {1..60}; do sleep 1 && x=$(ps -p $pid -o %cpu,%mem|grep ["."]);echo $i "  " $x; done >>file.txt
kill $pid
