import socket
import hmac

TLDS1_hostname = "ilab1.cs.rutgers.edu"
TLDS2_hostname = "ilab2.cs.rutgers.edu"


portc = 5000
portrs = 5001 #Port number at which RSserver listing on
TS1Port = 5005 #Port number at which TLDS1 listning on
TS2Port = 5006 #Port number at which TLDS2 listning on

end = "endconnection"

def readFile():
    dns_output = []
    f = open("PROJ3-HNS.txt", "r")
    for line in f:
        dns_output.append(line.rstrip())
    return dns_output

def DigestGenerator(key, challenge):
    d1 = hmac.new(key.encode(),challenge.encode("utf-8"))
    p = (d1.hexdigest())
    return p

def TLDS1(input_client, TS1):
    if(TS1 == None):
        try:
            TS1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            remote_name = socket.gethostname() #splits[0]
            #runs on different computer so need host name of that computer
            #Host name on which this TLDS server is: cpp.cs.rutgers.edu
#            remote_ip = socket.gethostbyname(TLDS1_hostname)
            # TLDS1_hostname = socket.gethostname()
            remote_ip = socket.gethostbyname(TLDS1_hostname)
            TS1.connect((remote_ip, TS1Port))
        except socket.error:
            print(socket.error)


    #print("Message send to TS1 server = ", input_client)
    TS1.send(input_client.encode('utf-8'))
    result1 = TS1.recv(100).decode('utf-8')
    if(result1 == "endconnection"):
        TS1.close()
        exit()

    return result1, TS1

def TLDS2(input_client, TS2):
    if(TS2 == None):
        try:
            TS2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            remote_name = socket.gethostname() #splits[0]
            #runs on different computer so need host name of that computer
            #Host name on which this TLDS server is: java.cs.rutgers.edu
#            remote_ip = socket.gethostbyname(TLDS2_hostname)
            # TLDS2_hostname = socket.gethostname()
            remote_ip = socket.gethostbyname(TLDS2_hostname)
            TS2.connect((remote_ip, TS2Port))
        except socket.error:
            print(socket.error)


    #print("Message send to TS2 server = ", input_client)
    TS2.send(input_client.encode('utf-8'))
    result1 = TS2.recv(100).decode('utf-8')
    if(result1 == "endconnection"):
        TS2.close()
        exit()

    return result1, TS2

def start_client(dns_entries):
    print("[Client]: DNS Entries on client are:", dns_entries)
    print("[Client]: Client started, sending message to S ...")
# Initialization
    TS2 = None
    input_client = "Hello From client"
    p, TS2 = TLDS2(input_client, TS2)

    TS1 = None
    input_client = "Hello From client"
    p, TS1 = TLDS1(input_client, TS1)


    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_name = socket.gethostname()
        local_ip = (socket.gethostbyname(local_name))
        rs.connect((local_ip, portrs))
    except socket.error:
        print(socket.error)


    f = open("RESOLVED.txt", "w")
    for i in dns_entries:
        splits = i.split()
        m = DigestGenerator(splits[0], splits[1])
        query = splits[2]
        Data = splits[1]+" "+m
        print("[Client]: Sending challenge string to Authentication Server: "+Data)
        rs.send(Data.encode('utf-8'))
        input_data = rs.recv(100).decode('utf-8')
        print("[Client]: recived host name of TLDS to connect: "+input_data)
        save = "Error Not Found!"
        if(input_data == TLDS1_hostname):
           # print("connect TLDS1")
            p, TS1 = TLDS1(query, TS1)
            save = "TLDS1" +" "+p

        elif(input_data == TLDS2_hostname):
#            print("connect TLDS2")
#            print(query)
            p, TS2 = TLDS2(query, TS2)
            save = "TLDS2" +" "+p
        else:
            print("[Client]: connect Nothing")
        f.write(save+"\n")
    print("[Client]: Closing")
    rs.send(end.encode('utf-8'))
    rs.close()

    #exit()

if __name__ == '__main__':
    dns_entries = readFile()
    start_client(dns_entries)
