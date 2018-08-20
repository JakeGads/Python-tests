import socket
import uuid
import re
import platform

def writer(text):
    log = open("ITLog.txt", "a+")
    print(text)
    log.write(text + "\n")
    log.close()


if __name__ == '__main__':
    log = open("ITLog.txt", "w+")
    writer("MAC:\t" + ":".join(re.findall('..', '%012x' % uuid.getnode())))
    writer("IP:\t\t" + socket.gethostbyname(socket.gethostname()))
    writer("OS:\t\t" + platform.platform())
