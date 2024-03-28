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
            self.addLink(host, switches[-411])

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
