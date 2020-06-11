# DNS Socket Programming Project  
In this project the DNS (Domain Name System) is implemented with the Authentication Server. The prject is divided into four different parts; client server, authentication server, and two TLDS (Top Level Domain Server). Each server communicate with each other using the sockets created between them. The client DNS uses a key and a challenge string to create a digest and sends the challenge string as well as the digest to the authentication server. Authentication server then sends only the challenge string to both TLDS servers, and in return TLDS servers send their respective digest for thee challenge string. Authentication server compares digest sent from Client with both diests sent by the TLDS, and decides which responce from TLDS server match the digest sent by client server. The Authentication server sends the hostname of the TLDS server with the correct match to the client. The DNS client then connects to that TLDS server with a query string and obtains the A record (if found) from the authenticated TLDS server.  
A brief sketch of the interaction among the programs can be shown as:   
<img src="/Images/Sketch.PNG">  
Both TLDS1 and TLDS2, each maintain a DNS_table consisting of three fields (hostname, IP adress, Flag) and a key which is use to create a digest from a challenge. When Client connects to the authentication server, it sends back the hostname of correctly matched digest TLDS. Using a returned hostname of the top level domain server, client makes connection to that TLDS server to get the IP adress of desired hostname. The TLDS server look up in it's DNS_table and if there is a mathch, sends the DNS table entry as  string, otherwise returns "Error: hOST NOT FOUND".  
### Usage
To run this project at least two different devices are required, since both TLDS servers can not be run on same device.



