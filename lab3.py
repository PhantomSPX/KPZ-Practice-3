
import re
import socket
import platform

def palindrom(input):
    if not isinstance(input, str):
        raise Exception("The argument must contain the string ")
    if len(input) < 2:
        raise Exception("The argument must contain a string of more than 2 characters")
    result = []
    array = re.findall(r"[\w']+", input)
    for value in array:
        if len(value) > 1:
            if len(value) > 1:
                if value == value[::-1]:
                    result.append(value)
    return result




def validate_ip(ip_address):
    if len(ip_address) < 7:
        raise Exception("The argument must contain a string of more than 7 characters")
    if not isinstance(ip_address, str):
        raise Exception("The argument must contain the string ")

    try:
        socket.inet_aton(ip_address)
        return True
    except:
        return False



def get_os():
    os = platform.system()
    if os == "Darwin":
        return "Mac"
    elif os == "Java":
        pass
    else:
        return os
