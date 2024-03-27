from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add switches
        switches = []
        for j in range(1, 413):
            switch = self.addSwitch('s{}'.format(j))
            switches.append(switch)

        # Add hosts
        hosts = []
        for i in range(1, 15):
            host = self.addHost('h{}'.format(i))
            hosts.append(host)

        # Connect switches in a linear manner
        for i in range(len(switches) - 1):
            self.addLink(switches[i], switches[i+1])

        # Connect the last switch to all hosts
        for host in hosts:
            self.addLink(host, switches[-1])

topos = {'mytopo': (lambda: MyTopo())}

if __name__ == '__main__':
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()

    # Assign IP addresses to hosts
    for i in range(1, 15):
        host = net.get('h{}'.format(i))
        host_ip = '10.0.0.{}'.format(i)
        host.setIP(host_ip, 24)

    # Add rules to allow any-to-any communication
    for switch in net.switches:
        switch_name = switch.name
        for other_switch in net.switches:
            other_switch_name = other_switch.name
            if switch_name != other_switch_name:
                switch.cmd('ovs-vsctl set bridge {} protocols=OpenFlow13'.format(switch_name))
                switch.cmd('ovs-vsctl set bridge {} protocols=OpenFlow13'.format(other_switch_name))
                switch.cmd('ovs-ofctl add-flow {} "priority=100, actions=output:{}"'.format(switch_name, other_switch_name))
                switch.cmd('ovs-ofctl add-flow {} "priority=100, actions=output:{}"'.format(other_switch_name, switch_name))
    # Allow icmp h1 to h14
    host1 = net.get('h1')
    host14 = net.get('h14')
    host14.cmd('iptables -A INPUT -p icmp --icmp-type echo-request -s 10.0.0.1 -j ACCEPT')
    host1.cmd('iptables -A OUTPUT -p icmp --icmp-type echo-request -d 10.0.0.14 -j ACCEPT')
    print(host1.cmd('ping -c 1 10.0.0.14'))
    net.stop()

