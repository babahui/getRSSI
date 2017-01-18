#!/bin/zsh

for (( i=0; i<=10; i++))
do
sudo iwlist wlp0s20f0u7 scanning | egrep 'Signal|SSID' | sed -e "s/\tSignal: //" -e "s/\tESSID: //" | sed 'N;s/\n/ /' | awk -F '=' '{print $3}' | awk -F ' ' '{print $1,$3}'  >> ../data/data-1-12/room504.txt
sleep 1
done

echo ' ' >> ../data/data-1-12/room504.txt

