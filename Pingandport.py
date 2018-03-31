import re
import socket
import subprocess
import string
import os
with open(os.devnull, "wb") as limbo:
    input_ip = raw_input('Enter the ip:')
    flag = 0
    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
    match = re.match(pattern, input_ip)
    punctuation_string = "!#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
    if((match) and not(any((let in input_ip) for let in (string.letters) ) or any((let in input_ip) for let in (punctuation_string) ) )):
        field = input_ip.split(".")
        for i in range(0, len(field)):
            if (int(field[i]) < 256):
                flag += 1
            else:
                flag = 0
    while((flag<4)or(flag>4)):
        input_ip = raw_input('Enter the ip:')
        flag = 0
        pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
        match = re.match(pattern, input_ip)
        if((match) and not(any((let in input_ip) for let in (string.letters) ))):
            field = input_ip.split(".")
            for i in range(0, len(field)):
                if (int(field[i]) < 256):
                    flag += 1
                else:
                    flag = 0

    hostIP = input_ip.rsplit('.', 1)[0]
    for n in xrange(50, 100):
        ip=hostIP+".{0}".format(n)
        result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                stdout=limbo, stderr=limbo).wait()
        if result:
                print ip, " is inactive"
        else:
                print ip, "is active"
                for port in range(1,400):
                    var_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = var_socket.connect_ex((ip, port))
                    if result == 0:
                        print format(port)
                    var_socket.close()




