import socket

TLDS1_hostname = "ilab1.cs.rutgers.edu"
TLDS2_hostname = "ilab2.cs.rutgers.edu"


RootServerPort = 5001; #Root port or aythentication server port
TS1Port = 5004 # TLDS1
TS2Port = 5003 # TLDS2
end = "endconnection"

def TLDS1_Server(input_client, TS1):
    if(TS1 == None):
        try:
            TS1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            remote_name = socket.gethostname() #splits[0]
            # TLDS1_hostname = socket.gethostname()
            remote_ip = socket.gethostbyname(TLDS1_hostname)
            TS1.connect((remote_ip, TS1Port))
            print("[RSserver]: Initialization of TLDS1 sucessful")
        except socket.error:
            print(socket.error)

    print("[RSserver]: Message send to TLDS1 server: "+ input_client)
    TS1.send(input_client.encode('utf-8'))
    result1 = TS1.recv(100).decode('utf-8')
    print("[RSserver]: Message Recived from TLDS1 server: "+result1)
    if(result1 == "endconnection"):
        print("[RSserver]: Closing TLDS1 server")
        TS1.close()
        # exit()

    return result1, TS1

def TLDS2_Server(input_client, TS2):
    if(TS2 == None):
        try:
            TS2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            remote_name1 = socket.gethostname() #splits[0]
            # TLDS2_hostname = socket.gethostname()
            remote_ip1 = socket.gethostbyname(TLDS2_hostname)
            TS2.connect((remote_ip1, TS2Port))
            result2 = "Initialization sucessful"
            print("[RSserver]: Initialization of TLDS2 sucessful")
        except socket.error:
            print(socket.error)

    print("[RSserver]: Message send to TLDS2 server: "+ input_client)
    TS2.send(input_client.encode('utf-8'))
    result2 = TS2.recv(100).decode('utf-8')
    print("[RSserver]: Message Recived from TLDS2 server: "+result2)

    if(result2 == "endconnection"):
        print("[RSserver]: Closing TLDS2 server")
        TS2.close()
        # exit()
    return result2, TS2


def startServer():
    print("[RSserver]: Server RS started, waiting for client(s)...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(socket.error)
    s.bind(('', RootServerPort))
    s.listen(1)
    local_name = socket.gethostname()
    local_ip = (socket.gethostbyname(local_name))
    conn, client_ip = s.accept()
    TS1 = None
    TS2 = None

    while True:
        input_client = conn.recv(100).decode('utf-8')
        if (input_client == "endconnection"):
            pm , TS2 = TLDS2_Server(input_client, TS2)
            p , TS1 = TLDS1_Server(input_client, TS1)
            s.close()
            exit()

        splits = input_client.split()
        result1 , TS1 = TLDS1_Server(splits[0], TS1)
        print("[RSserver]: Message Recived from TLDS1: ", result1)

        result2 , TS2 = TLDS2_Server(splits[0], TS2)
        print("[RSserver]: Message Recived from TLDS2: ", result2)

        if(result1 == splits[1]):
            result = "TS1 IS THE MATCH"
            back = TLDS1_hostname

        elif(result2 == splits[1]):
            result = "TS2 IS THE MATCH"
            back = TLDS2_hostname

        else:
            result = "NO MATCH"
            back = "NO MATCH"

        result1 , TS1 = TLDS1_Server(result, TS1)

        result2 , TS2 = TLDS2_Server(result, TS2)

        conn.send(back.encode('utf-8'))
#        print("Sending to the client:" + result)


 #   exit()


startServer()
