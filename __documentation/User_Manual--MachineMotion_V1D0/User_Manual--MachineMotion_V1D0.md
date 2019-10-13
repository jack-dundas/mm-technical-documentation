# User Manual: MachineMotion Controller

<p style="text-align:center;" ><img src="_media/machine_motion_user_manual_cover.png" width="100%" height="100%"></p>

## Introduction
MachineMotion is an all-in-one automation controller. It contains the necessary components to rapidly create general motion control and automation projects. Its embedded single-board computer, multi-function sensor inputs and connectivity options greatly simplify system setup time and configuration. On the software side, even users with limited programming experience can create automated machines.

This manual will explain how to setup, program and operate the MachineMotion controller. 

To best utilize this user guide, it is recommended to have a MachineMotion controller at hand. A computer with Google Chrome installed is also required.


## Table of Content
[TOC]


## Overview
As shown in *Figure 2* & *Figure 3*, MachineMotion contains several interfaces.

<p style="text-align:center;" ><img src="_media/CE-CL-105-0003_Front.png" width="45%" height="45%"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 2. MachineMotion Controller Front Plate</em></p>

### Device Interfaces
| Device Type                   | Ports                                                         |
|---                            |---                                                            |
| High power stepper motors     | DRIVE1, DRIVE2, DRIVE3                                        |
| End-of-Travel Sensors         | SENSOR1A, SENSOR1B, SENSOR2A, SENSOR2B, SENSOR3A, SENSOR3B    |
| Auxiliary                     | AUX1, AUX2, AUX3                                              |


### Connectivity Interfaces
| Connectivity Type             | Ports                                                         |
|---                            |---                                                            |
| One Cable Pendant             | PENDANT                                                       |
| Standard Ethernet             | ETHERNET                                                      |
| Fixed Ethernet                | 192.168.7.2                                                   |                            

### Safety interfaces
| Name                          | Description                                               | Ports Label   |
|---                            |---                                                        |---            |
| Safety System Input           | Input used to place the system in emergency stop mode     | SAFETY IN     | 
| Safety System Output          | Output used to trigger the system inputs of other devices | SAFETY OUT    |

<p style="text-align:center;" ><img src="_media/CE-CL-105-0003_Back.png" width="45%" height="45%"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 3. MachineMotion Controller Back Plate</em></p>  
    
For additional details on electrical specifications, consult the following online document [Datasheet – MachineMotion Controller](https://www.vention.io/technical-documents/machinemotion-controller-datasheet-10).

No software installation is required on your computer to start working with the MachineMotion controller. A computer with a web browser (preferable Google Chrome) is enough to access the controller, launch programs and control your machine.

### Important Notes

#### Links
Links in the sections below point directly to the MachineMotion controller. For these links to be functional, a controller must be connected to your computer via the fixed IP of the MachineMotion controller, 192.168.7.2.

#### Port Hosting the Controller Fixed IP

The default controller IP addresss was formerly hosted on the USB port. If your controller was purchased before 2019-06-01 you must connect your computer to the USB port to get access via this address.

## Installation

### Controller
### Stepper Motors
### End-Stop Sensors
### Encoders
### Digital IO Module
### Pendant

## Communicating with the Controller

MachineMotion offers several connection options to interact with external devices. More precisely, three communication methods are available.

- The 192.168.7.2 port (fomerly labelled DEFAULT ETHERNET)
- The ETHERNET port
- The PENDANT port

### Using the 192.168.7.2 port (Formerly labelled DEFAULT ETHERNET)
This method is mostly used to connect a computer to MachineMotion in a peer-to-peer way (one to one connection). It is also useful to have access to the system in case other ports are not available for use.
Connecting
Simply connect an Ethernet cable in the port that is labelled 192.168.7.2 (formerly labelled DEFAULT ETHERNET). If you do not have an Ethernet port on your computer, utilize the Ethernet to USB adapter provided with the controller.

<p style="text-align:center;" ><img src="_media/CE-CL-105-0003_Front_edited_192.168.7.2_port.png" width="45%" height="45%"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 4: The 192.168.7.2 pre-configured Ethernet port on the MachineMotion controller, in the green box.</em></p>

By default, the network adapter of your computer should be in DHCP mode and configure itself automatically.

#### Optional Details
The MachineMotion controller acts as a DHCP server on this port. When another device is connected, it assigns it the 192.168.7.1 address and auto assigns itself to 192.168.7.2. For this to properly function, your computer adapter settings must be set to DHCP (which is the default).

### Using the ETHERNET port
Using the ETHERNET port is useful when connectiong MachineMotion to a standard, multi-device Ethernet network. This use case becomes necessary when connecting multiple MachineMotion controllers together in multi-controller systems and when connecting MachineMotion on a LAN or WLAN.

<p style="text-align:center;" ><img src="_media/CE-CL-105-0003_Front_edited_Ethernet_port.png" width="45%" height="45%"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 5: The 192.168.7.2 pre-configured Ethernet port on the MachineMotion controller, in the green box.</em></p>

#### Connecting using DHCP
A DHCP client natively runs on the controller and will respond to DHCP commands from a DHCP server. Follow the steps below to configure your controller in DHCP mode.

- Step 1: Connect a computer to the 192.168.7.2 port (formerly DEFAULT ETHERNET) and browse to 192.168.7.2 using Google Chrome.

<p style="text-align:center;" ><img src="_media/ControlCenter_main_page.png" width="75%" height="75%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 6: MachineMotion ControlCenter Main Page</em></p>
 
- Step 2: Click on the Network Configuration tab.

<p style="text-align:center;" ><img src="_media/ControlCenter_network_config.png" width="75%" height="75%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 6: MachineMotion ControlCenter Main Page</em></p>
 
- Step 3: Click on “Use Dynamic Mode”

At this point, you will see the currently active IP address that the ETHERNET port was assigned in the ControlCenter fileds. You can ask your network administrator to assign rules to address your controller using its MAC address. To do the later, you will need to get the MAC address of the controller. Consult *Appendix B*.


#### Connecting using Static Mode
If the application requires the use of fixed IP addresses on your network, you can utilize a similar method to configure the MachineMotion controller.
In order to do so, some parameters of the Network need to be known. Usually, this is available from your system administrator or from the configuration utility of your network router.

- Step 1: Connect a computer to the 192.168.7.2 port (formerly DEFAULT ETHERNET) and browse to 192.168.7.2 using Google Chrome.

<p style="text-align:center;" ><img src="_media/ControlCenter_main_page.png" width="75%" height="75%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 8: MachineMotion ControlCenter Main Page</em></p>
 
- Step 2: Click on the Network Configuration tab.

<p style="text-align:center;" ><img src="_media/ControlCenter_network_config.png" width="75%" height="75%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 9: MachineMotion ControlCenter Main Page</em></p>

 
Step 3: Enter the IP, Netmask & Gateway fields and click on “Use Static Mode”.

#### Using the PENDANT
The MachineMotion pendant allows users to have a configuration free connection to the controller. Simply connect the pendant in the PENDANT port using its 8 pin M12 cable.


## Configuring Actuators
(Setup Guide for Linear Axes)
### Axis Direction & End-Stop Sensors

### Configuration Using the Vention ControlCenter

## Browser Based Services

### Cloud9 Integrated Development Environment (IDE)
For users that desire to access the single-board computer that is located inside the controller, the Cloud9 IDE is available on port 3000.

Cloud 9 essentially offers a terminal access and file explorer for developing software directly on the MachineMotion controller.

To access Cloud9, browse to [192.168.7.2:3000](http://192.168.7.2:3000) or <your_custom_machine_motion_ip>:3000.

<p style="text-align:center;" ><img src="_media/cloud_9.png" width="60%" height="60%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure X: Cloud 9 IDE</em></p>

#### Additional Details:

##### Root Credentials:
- password:  temppwd	

## Programming Options

## Controller Versions

## Related Documents
