import socket
import netifaces as nif


def getMac():
    print(mac_for_ip())
    return mac_for_ip()



def getIp():
    print(socket.gethostbyname(socket.gethostname()))
    return str(socket.gethostbyname(socket.gethostname()))


if __name__ == '__main__':
    networkLog += 'IP:\t' + getIp()
    networkLog = 'MAC:\t' + getMac(getIp())
    file = open('ITlog.txt', 'a+')


def mac_for_ip(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if_mac = addrs[nif.AF_LINK][0]['addr']
            if_ip = addrs[nif.AF_INET][0]['addr']
        except IndexError as KeyError:  # ignore if aces that don't have MAC or IP
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None
