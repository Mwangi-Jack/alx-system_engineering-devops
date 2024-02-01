# 0x07. Networking basics #0

## Internet

- This refers to a global system of interconnected computer networks that uses the TCP/IP protocol suite to communicate between networks and devices

- The Internet carries a vast range of information resources and services such as the interlinked hypertext documents and applications of the  world wide web (WWW)

## Local Area Network

- This is a computer network that interconnects computers  within a limited area such as a school or office building.

- Ethernet and Wi-fi are the two most common  technologies use fo LANs

## Wide Area Network

- This is a telecommunications network that exteds overa large geographical area.

- A telecommunication network is a group of nodes interconnected by telecommunication links that are use to exchange messages between the nodes.

## Iternet Protocol Suite (TCP/IP)

- A set of networking protocols that form the basis of the internet.

- It provides a framework for communication and data exchange between devices on a network

- The layers include;

 1. Application Layer
	* Provides network services directly to end-users or applications
	* Hosts application specific protocols for tasks such as email (SMTP),
	 file transfer (FTP), and domain name resolution (DNS)

 2. Transport Layer
	* Manages end-to-end communication and ensures reliable data delivery
	* Key protocols used by this layer include:
	  - TCP - For reliable and connection oriented communication
	  - UDP - For connectionless and less reliable communication

 3. Internet Layer
    * Responsible for addressing, routing, and fragmentation of data on the network
	* Key protocols used in this layer include
	  - Internet Control Message Protocl (ICMP)
	  - Internet Protocol (IP)

 4. Link layer
	* Defines protocols for the physical transmission of data on the network
	* Manages communication between devices on the same network


## The OSI Model

- The Open System Interconnection (OSI) Model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstract layers;

	1. Physical Layer
		* concerned with the pysical connection between devices.
		* Defines specifications such as voltage, cable types and data rates

	2. Data Link Layer
		* Provides error detection and correction over the pysical layer.
		* Responsible for framing, addressing and controlling access to the pysical medium.
		* Examples: Ethernet switches and Network Interface Cards (NICs)

	3. Network Layer
		* Manages routing and forwarding of data packets between devices
		* Adresses and routes data between source and destination devices

	4. Transport Layer
		* Ensures reliable datat transfer between devices.
		* Manages flow control, error correction, and re-transmission of lost or corrupted data.
		* Protocols used on this layer include TCP and UDP

	5. Session Layer
		* Establishes, manages and terminates sessions (connections) between applications
		* Responsible for dialogue control and synchronization between devices
		* Manages sessions checkpointing and recovery

	6. Presentation Layer
		* Translates data between the application layer and the lower layers.
		* Handles data compression, encryption, and character set conversion
		* Ensures data is in readable format for the application layer.

	7. Application Layer
		* Provides network services directly to end-users or applications.
		* Implements high-level protocols for tasks such as email, file transfer and network management.


## IP Address

- This is a numerical label assigned to each device connected to a computer network that uses internet protocol for communication.
- IP addresses serve two purposes;
	* Identifying the host or network interface
	* Providing the location of the host in the network
- IP addreses are of two versions

	### IPv4
	- It is the initial version used on the first generation of the internet and still is in use
	- consists of four sets of numbers separated by dots
	- Each set can range from 0-255 (8 bits) making a total of 32 bits
	- E.g. 192.168.0.1
	### IPv6
	- Introduces address limitations of IPv4 providing a much lager address space.
	- The address is represented in hexadecimal and separated by colons
	- It uses 128 bits for the IP address and was standardized in 1998
