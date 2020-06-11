import socket
import hmac

port = 5003
RootPort = 5006 #TLDS2 port number

def readFile():
    dns_output = []
    f = open("PROJ3-TLDS2.txt","r")
    for line in f:
        splits = line.split()
        dns_output.append([splits[0],splits[1], splits[2]])
    return dns_output

def get_dns(input_client, dns_entries):
    for i in dns_entries:
        if i[0] == input_client.strip():
            return i[0] + " " + i[1] + " " + i[2]
    return "Error: HOST NOT FOUND"



def startServer(dns_entries):
    #print("DNS Entries on TS are:", dns_entries)
    print("[TLDS2]: Server TS started, waiting for client(s)...")

    try:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(socket.error)
    s1.bind(('', RootPort))
    s1.listen(1)
    local_name = socket.gethostname()
    local_ip = (socket.gethostbyname(local_name))
    conn1, client_ip = s1.accept()
#initialization
    input_client = conn1.recv(100).decode('utf-8')
    conn1.send(input_client.encode('utf-8'))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(socket.error)
    s.bind(('', port))
    s.listen(1)
    local_name = socket.gethostname()
    local_ip = (socket.gethostbyname(local_name))
    conn, client_ip = s.accept()
    f = open("PROJ3-KEY2.txt", "r")
    key = f.read().split()[0]
#    key = "k6854"

    while True:
        input_client = conn.recv(100).decode('utf-8')
        if(input_client == "endconnection"):
            conn.send(input_client.encode('utf-8'))
            print("[TLDS2]: Closed")
            s.close()
            exit()
        else:
            d1 = hmac.new(key.encode(),input_client.encode("utf-8"))
            p = (d1.hexdigest())
            conn.send(p.encode('utf-8'))

            input_client = conn.recv(100).decode('utf-8')
            conn.send(p.encode('utf-8'))
            if(input_client == "TS2 IS THE MATCH"):
                print("[TLDS2]: Client will be connecting soon")
                input_client = conn1.recv(100).decode('utf-8')
                print(input_client)
                input_client = get_dns(input_client, dns_entries)
                conn1.send(input_client.encode('utf-8'))
if __name__ == '__main__':
    dns_entries = readFile()
    startServer(dns_entries)
