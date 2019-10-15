<p style="text-align:center;" ><img src="_media/machine_motion_user_manual_cover.png" width="100%" height="100%"></p>

<br>

<h3>Contents</h3>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#connecting-components">Connection Components</a></li>
        <li><a href="#software-installation">Software Installation</a></li>
        <li><a href="#communicating-with-the-controller">Communicating with the Controller</a></li>
        <li><a href="#actuator-software-configuration">Actuator Software Configuration</a></li>
        <li><a href="#actuator-hardware-configuration">Actuator Hardware Configuration</a></li>
        <li><a href="#cloud9-integrated-developement-environment-ide">Cloud9 Integrated Development Environment (IDE)</a></li>
        <li><a href="#programming-options">Programming Options</a></li>
        <ul>
            <li><a href="#machine-logic">MachineLogic</a></li>
            <li><a href="#machine-logic">Python</a></li>
        </ul>
    </ul>
    
<br>

### Overview
MachineMotion is an all-in-one automation controller. It contains the necessary components to rapidly create general motion control and automation projects. Its embedded single-board computer, multi-function sensor inputs and connectivity options greatly simplify system setup time and configuration. On the software side, even users with limited programming experience can create automated machines.

<br>

### Important Notes
- Direct hyperlinks in the sections below point directly to the MachineMotion controller. For these hyperlinks to be functional, a controller must be connected to your computer via the fixed IP of the MachineMotion controller, 192.168.7.2.

- On previous versions of the controller, the IP default IP address was hosted on the USB connector. If your controller was purchased before 2019-06-01 you must connect your computer to the USB connector to get access via this address. For controllers purchased after 2019-06-01, the connector labelled 192.168.7.2 or DEFAULT ETHERNET must be used.

<br>

### Connecting Components
As shown in Figure 2 & Figure 3, MachineMotion contains several connectors on its front panel. Each connector is meant to be used for certain device types. The tables below detail where to connect different devices.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/033/large/mmum-ce-cl-105-0003-front.png?1571111330" width="45%" height="45%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 2. MachineMotion Controller Front Panel</em></p>

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/032/large/mmum-ce-cl-105-0003-back.png?1571111327" width="45%" height="45%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 3. MachineMotion Controller Back Panel</em></p>  

<br>

[comment]: <> (Table -- Vention Automation Components)

<h4 style="font-weight: bold;" id="vention-automation-components"><a class="anchor" href="vention-automation-components"><span class="octicon octicon-link"></span></a>Vention Automation Components</h4>
    <div style="border: 2px solid #E9ECEF;padding: 5px;width:80%; margin: auto; font-size:90%">
    <table class="table" style="width:95%; margin: auto">
        <tbody>
            <tr valign="top" style="font-weight:strong;">
                <td style="border-top: 0px; width: 34%"><strong>Device</a></strong></td>
                <td style="border-top: 0px; width: 33%"><strong>Vention Part Number</a></strong></td>
                <td style="border-top: 0px; width: 33%"><strong>MachineMotion Connnector</strong></td>
            </tr>
            <tr>
                <td><strong>Stepper Motors</strong></td>
                <td>MO-SM-00_-0001</td>
                <td>DRIVE1 DRIVE2 DRIVE3</td>
            </tr>
            <tr>
                <td><strong>End-of-Travel Sensors</strong></td>
                <td>CE-SN-004-0001</td>
                <td>SENSOR1_ SENSOR2_ SENSOR3_</td>
            </tr>
            <tr>
                <td><strong>Encoder</strong></td>
                <td>CE-SN-002-0001</td>
                <td>AUX1 AUX2 AUX3</td>
            </tr>
            <tr>
                <td><strong>Digital IO Module</strong></td>
                <td>CE-MD-001-0001</td>
                <td>AUX1 AUX2 AUX3</td>
            </tr>
            <tr>
                <td><strong>Power-Off Brake</strong></td>
                <td>MO-PT-002-0001</td>
                <td>AUX1 AUX2 AUX3</td>
            </tr>
        </tbody>
    </table>
    </div>
<br>

[comment]: <> (Table -- HMI and Computers)

<h4 style="font-weight: bold;" id="hmi-and-computers"><a class="anchor" href="hmi-and-computers"><span class="octicon octicon-link"></span></a>HMI and Computers</h4>
    <div style="border: 2px solid #E9ECEF;padding: 5px;width:80%; margin: auto; font-size:90%">
    <table class="table" style="width:95%; margin: auto">
        <tbody>
            <tr valign="top" style="font-weight:strong;">
                <td style="border-top: 0px; width: 51%"><strong>Device</a></strong></td>
                <td style="border-top: 0px; width: 50%"><strong>MachineMotion Connector</a></strong></td>
            </tr>
            <tr>
                <td><strong>Stepper Motors</strong></td>
                <td>MO-SM-00_-0001</td>
            </tr>
            <tr>
                <td><strong>End-of-Travel Sensors</strong></td>
                <td>CE-SN-004-0001</td>
            </tr>
            <tr>
                <td><strong>Encoder</strong></td>
                <td>CE-SN-002-0001</td>
            </tr>
            <tr>
                <td><strong>Digital IO Module</strong></td>
                <td>CE-MD-001-0001</td>
            </tr>
        </tbody>
    </table>
    </div>
<br>

[comment]: <> (Table -- Saefty Devices)

<h4 style="font-weight: bold;" id="safety-devices"><a class="anchor" href="safety-devices"><span class="octicon octicon-link"></span></a>Safety Devices</h4>
    <div style="border: 2px solid #E9ECEF;padding: 5px;width:80%; margin: auto; font-size:90%">
    <table class="table" style="width:95%; margin: auto">
        <tbody>
            <tr valign="top" style="font-weight:strong;">
                <td style="border-top: 0px; width: 34%"><strong>Device</a></strong></td>
                <td style="border-top: 0px; width: 33%"><strong>Description</a></strong></td>
                <td style="border-top: 0px; width: 33%"><strong>MachineMotion Connector</a></strong></td>
            </tr>
            <tr>
                <td><strong>Safety System Input</strong></td>
                <td>Input used to place the system in emergency stop mode</td>
                <td>SAFETY IN</td>
            </tr>
            <tr>
                <td><strong>Safety System Output</strong></td>
                <td>Output used to trigger the system inputs of other devices</td>
                <td>SAFETY OUT</td>
            </tr>
        </tbody>
    </table>
    </div>
<br>

For additional details on electrical specifications, consult the [MachineMotion Datasheet](https://www.vention.io/technical-documents/machinemotion-controller-datasheet-10).

<br>

### Software Installation
No software installation is required on your computer to start working with the MachineMotion controller. A computer with Google Chrome installed is enough to access the controller, launch programs and control your machine. If you are planning to use Python to create application programs, refer to the [Python API](https://www.vention.io/technical-documents/python-api-for-machinemotion-69) to get more details on software installation for this programming option.

<br>

### Communicating with the Controller

MachineMotion offers several connection options to interact with external devices. More precisely, three communication methods are available.

<h4></h4>
    <ul>
        <li>Peer-to-Peer Ethernet with Fixed IP</li>
        <ul>
            <li>192.168.7.2 connector</li>
        </ul>
        <li>Standard Ethernet</li>
        <ul>
            <li>ETHERNET connector</li>
        </ul>
        <li>MachineMotion Pendant</li>
        <ul>
            <li>PENDANT connector</li>
        </ul>
    </ul>
    <br>

#### Method 1: Peer-to-Peer Ethernet with Fixed IP
This is the best way to initially get started. This method is mostly used to connect a computer to MachineMotion in a peer-to-peer way (one to one connection). It is also useful to have access to the system in case other ports are not available for use.

Simply connect an Ethernet cable in the connector labelled 192.168.7.2 and to your computer. If you do not have an Ethernet port on your computer, utilize the Ethernet to USB adapter provided with the controller.

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/034/large/mmum-ce-cl-105-0003-front-edited-192-168-7-2-port.png?1571111333" width="45%" height="45%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 4: The 192.168.7.2 pre-configured Ethernet port on the MachineMotion controller, in the green box.</em></p>

<br>

By default, the network adapter of your computer should be in DHCP mode and configure itself automatically.

<br>

**Additional Details**
<br>
The MachineMotion controller acts as a DHCP server on this address. When another device is connected, it assigns it the 192.168.7.1 address and auto assigns itself to 192.168.7.2. For this to properly function, your computer adapter settings must be set to DHCP (which is the default).

<br>

#### Method 2: Standard Ethernet
Using the ETHERNET port is useful when connectiong MachineMotion to a standard, multi-device Ethernet network. This use case becomes necessary when connecting multiple MachineMotion controllers together in multi-controller systems and when connecting MachineMotion on a LAN or WLAN.

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/035/large/mmum-ce-cl-105-0003-front-edited-ethernet-port.png?1571111336" width="45%" height="45%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 5: The standard configurable ETHERNET connector.</em></p>

<br>

**DHCP Mode**

A DHCP client natively runs on the controller and will respond to DHCP commands from a DHCP server. Follow the steps below to configure your controller in DHCP mode.

- Step 1: Connect a computer to the 192.168.7.2 port (formerly DEFAULT ETHERNET) and browse to 192.168.7.2 using Google Chrome.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/042/large/mmum-controlcenter-main-page.png?1571111346" width="75%" height="75%" <img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 6: MachineMotion ControlCenter Main Page</em></p>

<br>
 
- Step 2: Click on the Network Configuration tab.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/043/large/mmum-controlcenter-network-config.png?1571111347" width="75%" height="75%" <img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 6: MachineMotion ControlCenter Main Page</em></p>

<br>

- Step 3: Click on “Use Dynamic Mode”

<br>

At this point, you will see the currently active IP address that the ETHERNET port was assigned in the ControlCenter fileds. You can ask your network administrator to assign rules to address your controller using its MAC address. To do the later, you will need to get the MAC address of the controller. Consult *Appendix B*.

<br>

**Static Mode**

If the application requires the use of fixed IP addresses on your network, you can utilize a similar method to configure the MachineMotion controller.
In order to do so, some parameters of the Network need to be known. Usually, this is available from your system administrator or from the configuration utility of your network router.

- Step 1: Connect a computer to the 192.168.7.2 port (formerly DEFAULT ETHERNET) and browse to 192.168.7.2 using Google Chrome.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/042/large/mmum-controlcenter-main-page.png?1571111346" width="75%" height="75%" img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 8: MachineMotion ControlCenter Main Page</em></p>

<br>
 
- Step 2: Click on the Network Configuration tab.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/043/large/mmum-controlcenter-network-config.png?1571111347" width="75%" height="75%" <img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 9: MachineMotion ControlCenter Main Page</em></p>

<br>
 
Step 3: Enter the IP, Netmask & Gateway fields and click on “Use Static Mode”.

<br>

#### Method 3: MachineMotion Pendant
The MachineMotion pendant allows users to have a configuration free connection to the controller. Simply connect the pendant in the PENDANT connector using its 8 pin M12 cable.

<br>

### Actuator Software Configuration

The section below will give detailed information on how motors, end-of-travel sensors and linear axes are configured in a Vention system.

<br>

**Note on Homing**

For motion control to be possible, a position reference must exist. This is what homing refers to, the action of finding the position reference of an axis. This position reference is also called home or zero.

End-of-travel sensors are used to perform homing operations. In order for the homing to be properly done, end-of-travel sensors must be placed in the appropriate location and connected to the right connector on the MachineMotion controller. Installation of end-stop sensors also depends on how the motor is installed on the linear axis.

<br>

**Software Configuration**

To operate an axis, it must first be configured software-wise. This is necessary to tell the system what is being moved. This can be done via the configuration tab in ControlCenter, see Figure 10.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/038/large/mmum-control-center-configuration-tab-edited.png?1571111339" width="75%" height="75%" img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 10: ControlCenter Axis Configuration Tab</em></p>

<br>

The configuration parameters of each axis can be changed independently as seen in Figure 11.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/040/large/mmum-control-center-configuration-view-edited.png?1571111342" width="75%" height="75%" img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 11: ControlCenter Axis Configuration Tab</em></p>

<br>

The important parameters to configure are:

<h4></h4>
    <ul>
        <li>Axis Mechanical Gain</li>
        <ul>
            <li>mm / turn or deg / turn</li>
        </ul>
        <li>Micro-Stepping Configuration</li>
        <ul>
            <li>8 by default</li>
        </ul>
        <li>Positive Motor Rotation Direction</li>
        <ul>
            <li>clockwise by default</li>
        </ul>
    </ul>

[comment]: <> (Table -- Actuator Mechanical Gains)

<br>

<h4 style="font-weight: bold;" id="actuator-mechanical-gains"><a class="anchor" href="actuator-mechanical-gains"><span class="octicon octicon-link"></span></a>Actuator Mechanical Gains</h4>
    <div style="border: 2px solid #E9ECEF;padding: 5px;width:80%; margin: auto; font-size:90%">
    <table class="table" style="width:95%; margin: auto">
        <tbody>
            <tr valign="top" style="font-weight:strong;">
                <td style="border-top: 0px; width: 51%"><strong>Actuator</a></strong></td>
                <td style="border-top: 0px; width: 50%"><strong>Mechnical Gain</a></strong></td>
            </tr>
            <tr>
                <td><strong>Ballscrew</strong></td>
                <td>10 mm / turn</td>
            </tr>
            <tr>
                <td><strong>Timing Belt</strong></td>
                <td>150 mm / turn</td>
            </tr>
            <tr>
                <td><strong>Electric Cylinder</strong></td>
                <td>6 mm / turn</td>
            </tr>
            <tr>
                <td><strong>Rack & Pinion</strong></td>
                <td>157.08 mm / turn</td>
            </tr>
            <tr>
                <td><strong>Rotary Indexer</strong></td>
                <td>85 deg / turn</td>
            </tr>
        </tbody>
    </table>
    </div>
<br>

### Actuator Hardware Configuration

<br>

**Motor Rotation Direction**

By convention, motors have a positive and a negative rotation direction. This is an important consideration when installing the motor on a linear axis. When sending motion commands to the controller (for example a relative move of +200mm), it is important that the axis moves in the desired direction.

The rotation direction convention is shown in Figure 12 and Figure 13.

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/881/large/positive_motor_direction.png?1548034463" width="25%" height="25%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 12: Motor Positive Rotation</em></p>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/882/large/negative_motor_direction.png?1548034476" width="25%" height="25%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 13: Motor Negative Rotation</em></p>

<br>

**Linear Axis Direction**

In order to satisfy the application requirements, positive rotation of the motor shaft should result in linear motion in the desired direction. Figures 14 show how the linear axis move depending on where the motor is installed.

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/048/large/mmum-positive-axis-direction-quadrant-3.png?1571111356" width="60%" height="60%"></p>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/047/large/mmum-positive-axis-direction-quadrant-2.png?1571111354" width="60%" height="60%"></p>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/046/large/mmum-positive-axis-direction-quadrant-1.png?1571111351" width="60%" height="60%"></p>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/049/large/mmum-positive-axis-direction-quadrant-4.png?1571111357" width="60%" height="60%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 14: Axis Direction Based on Motor Location</em></p>

<br>

**End-of-Travel Sensors**

Linear axes require the use of end-of-travel sensors, for two main reasons:
- Perform homing operations (placing the axis in a known position, called home or zero)
- Disable motion in the event of an over or under travel event.

Inductive sensors are the preffered option for end-of-travel sensing since they are non-contact and less subject to environmental interference.

- M18 Inductive Proximity Sensor (Sn = 10 mm): [CE-SN-004-0001](https://www.vention.io/parts/244)


The image below details how to connect and position the end-of-travel sensors for a specific motor position. Important points:

- The *home* sensor is positioned such that a negative motion moves towards it
- The *home* sensor is connected to port SENSOR1A 
- The *over-travel* sensor is positioned such that a positive motion moves towards it
- The *over-travel* sensor is connected to port SENSOR1B

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/051/large/mmum-sensor-connection-example.png?1571111360" width="60%" height="60%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 15: End-of-travel Sensors Connection</em></p>

<br>

**Direction Reversal**

It is posible that for design reasons, the motor has to be placed at a specific place on the linear axis (due to space or mechnical constraints). This could result in an undesired positive motion direction of the linear axis. For this reason, there is a also a software command that permits reversing the direction of a given axis. The ControlCenter configuration tab contains this parameter, as shown below in Figure 16.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/041/large/mmum-control-center-configuration-view-reverse-edited.png?1571111344" width="75%" height="50%" img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 16: Axis Direction Reversal in ControlCenter</em></p>

<br>

**++This configuration reverses the motor default rotation direction, but also reverses the position of the home and over-travel sensors.++**

Going back to the example of Figure 15, reversing the axis results in the following configuration.

- The *home* sensor is positioned such that a negative motion moves towards it
- The *home* sensor is connected to port SENSOR1B 
- The *over-travel* sensor is positioned such that a positive motion moves towards it
- The *over-travel* sensor is connected to port SENSOR1A

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/052/large/mmum-sensor-connection-example-reverse-direction.png?1571111363" width="60%" height="60%" ></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 17: End-of-travel Sensors Connection in Reversed Mode</em></p>

<br>

### Cloud9 Integrated Development Environment (IDE)
For users that desire to access the single-board computer that is located inside the controller, the Cloud9 IDE is available on port 3000.

Cloud 9 essentially offers a terminal access and file explorer for developing software directly on the MachineMotion controller.

To access Cloud9, browse to [192.168.7.2:3000](http://192.168.7.2:3000) or <your_custom_machine_motion_ip>:3000.

<br>

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/002/036/large/mmum-cloud-9.png?1571111338" width="60%" height="60%" <img style="border:1px solid grey;"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 18: Cloud 9 IDE</em></p>

**Additional Details**
- password:  temppwd	

### Programming Options

<br>

#### MachineLogic
The MachineLogic programming interface is a simple code-free programming tool for MachineMotion. Click [here](http://192.168.7.2/_pendant/vse.html) for a direct link to MachineLogic on your MachineMotion controller.

<br>

#### Python Programs
Refer to the latest [Python API](https://github.com/VentionCo/mm-python-api) for details on how to create programs for MachineMotion using Python.
