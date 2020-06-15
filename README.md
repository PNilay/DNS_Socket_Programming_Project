# DNS Socket Programming Project  
In this project the DNS (Domain Name System) is implemented with the Authentication Server. The project is divided into four different parts; client server, authentication server, and two TLDS (Top Level Domain Server). Each server communicates with each other using the sockets created between them. 
* The client DNS uses a key and a challenge string to create a digest and sends the challenge string as well as the digest to the authentication server. 
* Authentication server then sends only the challenge string to both TLDS servers, and in return TLDS servers send their respective digest for the challenge string. Authentication server compares digest sent by Client with digests sent by the TLDS, and decides which response matches the digest sent by client server from TLDS server. If matched, the Authentication server sends the hostname of the TLDS server to the client else sends "No Match Found".
* The DNS client then connects to that TLDS server with a query string and obtains a record (if found) from the authenticated TLDS server.   
A brief sketch of the interaction among the programs can be shown as:   
<img src="/Images/Sketch.PNG">  
Both TLDS1 and TLDS2, each maintain a DNS_table consisting of three fields (hostname, IP address, Flag) and a key which is used to create a digest from a challenge. When Client connects to the authentication server, it sends back the hostname of correctly matched digest TLDS. Using a returned hostname of the top level domain server client makes connection to that TLDS server and get the IP address of desired hostname. The TLDS server looks up in it's DNS_table and if there is a match, sends the DNS table entry as a string, otherwise returns "Error: HOST NOT FOUND".  
### Usage
To run this project at least two different devices are required, since both TLDS servers can not be run on the same device.  
First change the hostname of the TLDS1 and TLDS2 servers in Client.py (line 4 and 5), and RSserver (line 3 and 4) with your own hostnames. Start the two TLDS servers, then the Authentication server and lastly the client program form the command lines.  
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

