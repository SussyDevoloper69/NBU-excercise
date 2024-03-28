#!/bin/bash
curl http://localhost:8080/wm/firewall/module/enable/json -X PUT -d ''
curl -X POST -d '{"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.14/32", "dl-type":"ARP" }' http://localhost:8080/wm/firewall/rules/json
curl -X POST -d '{"src-ip": "10.0.0.14/32", "dst-ip": "10.0.0.1/32", "dl-type":"ARP" }' http://localhost:8080/wm/firewall/rules/json
curl -X POST -d '{"src-ip": "10.0.0.1/32", "dst-ip": "10.0.0.14/32", "nw-proto":"ICMP" }' http://localhost:8080/wm/firewall/rules/json
curl -X POST -d '{"src-ip": "10.0.0.14/32", "dst-ip": "10.0.0.1/32", "nw-proto":"ICMP" }' http://localhost:8080/wm/firewall/rules/json
sudo docker exec -it project-mininet-1 bash -c 'mn --custom /scripts/mininet.py --topo mytopo --controller=remote,ip=floodlight,port=6653'
