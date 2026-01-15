import socket

def is_port_open(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((host, port))
        sock.close()
        return True
    except:
        return False
