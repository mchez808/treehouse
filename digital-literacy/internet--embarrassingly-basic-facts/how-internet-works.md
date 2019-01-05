
History

1960s:
- Advanced Research Project Agency (ARPA)
- invention of packet switching
- 1969: ARPANET
1991: WWW


# TCP/IP

TCP is the transmission control protocol and it splits data up into packets and
puts them back together again at their destination.
IP, the internet protocol, tells the packets where to go and
to where they should return.

A packet isn't an entire web page, or even usually a whole e-mail.
It's a small chunk of data, like a puzzle piece of the whole picture.
By breaking data into these small,
manageable chunks, many users can transmit data at the same time very quickly.
In essence, these packets are a way of sharing access to the network, so
that no single transmission dominates the pipeline.


## TCP/IP vs HTTP

After opening up a web browser and typing in a URL, your browser uses a special
protocol called HTTP or Hyper Text Transfer Protocol.
This is a set of rules for asking for and getting webpages.

But there's an even more basic set of protocols under this, called TCP/IP.
Which is short for Transmission Control Protocol and Internet Protocol.
These are the rules for sending and receiving any data whether it's email, webpages or files on the Internet.
Once you initial your request TCP IP protocols take your request,
webpages, videos, or emails and break them into little packets of data and
send them in the fastest way possible. From client to server and back again.


After you request a web page TCP IP send your request wirelessly over
radio waves either to a router or directly to a wireless modem.
If you have a router what was a wireless request
is now sent along an ethernet chord to your modem.
Your modem then sends the packets along a coaxial cable or
phone line to the outside of your house where your internet service provider or
ISP connects you to the Internet.
The main network made of fiber optic cables and computers.

## added note on TCP/IP vs HTTP

One thing to bear in mind is you usually use both at the same time. Each one does a different job. The jobs they do is what primarily distinguishes them.

TCP/IP is for getting bits of data from one place to another. It's only concerned with connecting computers to each other and moving the data, not about what kind of data it is. So when you are using the web, it makes sure that the data bits coming from the server get to your machine, without errors, and in the order they were sent. It is called a "transport protocol". Think of it like a post office delivery truck.

HTTP is a kind of data packaging used by your browser, and web servers. It's not involved with delivery, just with what you have after the delivery arrives. Because it pertains to your application (program) it is called an "application protocol". Think of it as the envelope or the parcel.

### analogy

HTTP = Envelope/Parcel, IP = Post Office, TCP = Delivery Truck

HTTP is a protocol within the Application Layer of the TCP/IP stack...so to put it in different terms, HTTP is part of that relay process sending your message from your computer out over the network to get info and back again.

# Clients and Servers

Apache server is a webpage server , and FTP Server is a File server, used when you request a file.

An Apache server runs on the Linux / Unix Operating System.
