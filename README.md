# DNS Socket Programming Project  
In this project the DNS (Domain Name System) is implemented with the Authentication Server. The project is divided into four different parts; client server, authentication server, and two TLDS (Top Level Domain Server). Each server communicates with each other using the sockets created between them. The client DNS uses a key and a challenge string to create a digest and sends the challenge string as well as the digest to the authentication server. Authentication server then sends only the challenge string to both TLDS servers, and in return TLDS servers send their respective digest for the challenge string. Authentication server compares digest sent from Client with both digests sent by the TLDS, and decides which response from TLDS server matches the digest sent by client server. The Authentication server sends the hostname of the TLDS server with the correct match to the client. The DNS client then connects to that TLDS server with a query string and obtains the A record (if found) from the authenticated TLDS server.  
A brief sketch of the interaction among the programs can be shown as:   
<img src="/Images/Sketch.PNG">  
Both TLDS1 and TLDS2, each maintain a DNS_table consisting of three fields (hostname, IP address, Flag) and a key which is used to create a digest from a challenge. When Client connects to the authentication server, it sends back the hostname of correctly matched digest TLDS. Using a returned hostname of the top level domain server, client makes connection to that TLDS server to get the IP address of desired hostname. The TLDS server looks up in it's DNS_table and if there is a match, sends the DNS table entry as a string, otherwise returns "Error: HOST NOT FOUND".  
### Usage
To run this project at least two different devices are required, since both TLDS servers can not be run on the same device.  
First change the hostname of the TLDS1 and TLDS2 servers in Client.py (line 4 and 5), and RSserver (line 3 and 4) with your own hostnames. Start the two TLDS servers, then the Authentication server and then the client program, form the command lines.  
```
python TLDS1.py
```
```
python TLDS2.py
```
```
python RSserver.py
```
```
python Client.py
```
The hostname along with the key of TLDS server is given one per line in a file "PROJ3_HNS.txt" (Input to this program). Files PROJ3-KEY1.txt" and "PROJ2-KEY2.txt" stores the key of the TLDS server (without this key client can not request the IP address of desired hostname), which is used by the TLDS programs. "PROJ3-TLDS1.txt" and "PROJ3-TLDS2.txt" stores the hostname along with its ip address, from which TLDS servers provides the ip address of desired hostname to client server. The client program output the result of the "PROJ3_HNS.txt" to a file "RESOLVED.txt".



