#!/usr/bin/python3
"""
write a python script for nc command in linux for scanning a range of
ports for a specific ip passed during running of the script on cmdline
document per pep8
"""

import sys
import socket


def port_scanner(ip, port):
    """
    function to scan a port for a specific ip
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Port {}: Open".format(port))
        else:
            print("Port {}: Closed".format(port))
    except socket.error:
        print("Couldn't connect to server")
    sock.close()


def main():
    """
    main function
    """
    if len(sys.argv) != 3:
        print("Usage: python3 port_scanner.py <ip> <port>")
        sys.exit()
    ip = sys.argv[1]
    port = int(sys.argv[2])
    port_scanner(ip, port)


if __name__ == "__main__":
    main()
