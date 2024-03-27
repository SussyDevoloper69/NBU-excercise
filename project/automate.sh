#!/bin/bash
sudo docker exec -it project-mininet-1 bash -c 'mn --custom /scripts/mininet.py --topo mytopo --controller=remote,ip=floodlight,port=6653'
