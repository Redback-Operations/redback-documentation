---
sidebar_position: 7
---

# Virtual Private Cloud

Research Piece

In collaboration with DevOps team, find out how to deploy instances in private subnets and place a NAT gateway in front of those private subnets. This will hide the VM’s from the internet and still give them internet access for software updates.  
This task needs extensive research about VPC, subnets, difference between public and private subnets, and NAT gateway. 
 
Cyber Security team is expected to come back with an architecture diagram for the VPC which will then be deployed and tested by the DevOps team. 

## Virtual Private Clouds

### What is it?

- A virtual private cloud is a private cloud computing environment contained within a public cloud.

- A virtual private cloud allows for users to run code, store data, host websites and do anything they can in a normal private cloud, instead it is hosted by a public cloud.

### How it works

- The best features of private and public cloud systems are integrated in a virtual private cloud (VPC). When running on a public or shared architecture, VPCs perform like a private cloud.
- VPC has been most frequently utilised in the environment of cloud "infrastructure as a service" (IaaS), where a provider provides the basic public cloud infrastructure and various vendors may provide the VPC services offered over this infrastructure.
- A provider, such as Amazon AWS or Google, provides a public cloud infrastructure to be used with their provided VPC service. 
- From there, the provider allows access to a VPC, where they ensure that their customers data is kept separated from their other customers data.
- They can achieve this using a variety of different elements. These include:
    - Private IP addresses (subnets) – By using private IPs that are not accessible via the public internet, the VPC is very secure.
    - Encryption – By using VPNs to encrypt and create a private network above the public network. The VPN traffic is scrambled and invisible to other users.

### Benefits to using it

- There are many benefits to using VPCs, some of these include:
    - Agility – When using a VPC, users have full control of the network size, where their resourced can be scaled dynamically in real time
    - Security – Due to it being a virtual private cloud, user’s data and space don’t mix with other users of the cloud. This allows for users to control how their resources are accessed and by who.
    - Performance increase – When hosting websites and apps on their private cloud, they have a better performance than ones that are hosted on traditional physical servers
    - Hybrid clouds - It’s relatively easy to connect a VPC to a public cloud – or to on-premises cloud architecture via a VPN.

### Conclusion

- In conclusion, VPC is a real helpful tool that can be used to perform several tasks and should be considered by the DevOps team going forward.


## Subnets

### What is it?

- Subnet, short for subnetworks is a subdivision or a part of an IP network. It is essentially as network that is inside of another network.
- Subnets allow for networks to be more efficient and therefore overall make the entire network better.

### How it works

- A network is split into many different subnets. By splitting a network like this, network traffic must travel a much smaller distance and doesn’t have to pass through any unnecessary routers to get to where it needs.
- A network being divided into sub-networks can be described by the below image.

### Benefits to using it

- There are many benefits that arise when using subnets, some of these are the following:
    - Efficiency – Using subnets is far more efficient than not using subnets, when using them, traffic travels a much smaller and quicker distance, making it more efficient than not using them.
    - Isolating threats – By subnetting your network, you can more easily identify and locate any security threats, as you can isolate any compromised networks. From there you can prevent any more damage happening to your network.
    - Control network growth - When planning and designing a network, size is something that needs to be taken into consideration. One of the key benefits of subnetting is that it enables you to control the growth of your network.

### Conclusion

- Subnetting is a very beneficial thing as it can make both a network quicker and more secure, and therefore should seriously be considered to use going forward in the project.

## NAT Gateway

### What is it?

- NAT gateway is a Network Address Translation service that is used to connect instances in a private subnet to services outside of a VPC. However, the external services cannot establish a connection with the instances. 

### How it works

- A NAT gateway forwards the traffic from the instances that are in the private subnet to the internet / services and then sends the response back to the instance.
- When the traffic moves to the internet a IPv4 address is replaced with the NATs address.
- After the response is obtained, it is sent to the instance and the NAT translates the address back to the IPv4.
- A video describing a NAT gateway in further detail can be found below:
https://www.youtube.com/watch?v=ujXr0i5EoHE&ab_channel=CloudAcademy

## Public vs Private Subnets

### Public subnet

- A public subnet is a subnet that has a route table, and with that route table has a route to an internet gateway.
- This allows for the VPC to be able to connect both to the internet as well as other external services.
- Using a public subnet is a must, as it allows for internet connection as well as connection to the services, something that cannot be done with a private subnet.

### Private subnet

- A private subnet is a subnet that has a route table; however, it doesn’t not have a route to the internet gateway.
- Instances that are in the private subnet are usually backend server that don’t accept any traffic from the internet.
- Using a private subnet is a must as it acts as a security boundary for the public subnet. You can control a private subnet through different security groups of the public subnet. So if your public subnet was hacked it will ne harder to hack into the instances of the private subnets.


Using both is a must.

## References

https://www.ringcentral.com/gb/en/blog/definitions/virtual-private-cloud/
https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/
https://www.accessagility.com/blog/benefits-of-subnetting#:~:text=Subnetting%20is%20the%20practice%20of,control%2C%20and%20improving%20network%20security.
https://www.youtube.com/watch?v=ujXr0i5EoHE&ab_channel=CloudAcademy

