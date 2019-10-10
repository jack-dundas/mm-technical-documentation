## Digital IO Module Datasheet

<p style="text-align:center;" ><img src="_media/VEN_Parts_CE-MD-001-0001_01.png" width="75%" height="75%"></p>

### Contents
- Overview
- Important Notes
- Technical Specifications
- Applications
- Connecting to MachineMotion
- Control

### Overview
The Digital IO Module, CE-MD-001-0001 extends the functionality of the MachineMotion controller with 4 industrial 24V inputs and 4 industrial 24V outputs. It is a plug-&-play module that only requires a single connection to MachineMotion controller. It comes ready to use with its associated 5 meters M12 cable.

### Important Notes

#### Links
Links in the sections below point directly to the MachineMotion controller. For these links to be functional, a controller must be connected to your computer via the fixed IP of the MachineMotion controller, 192.168.7.2.

#### Port Hosting the Controller Fixed IP

The default controller IP addresss was formerly hosted on the USB port. If your controller was purchased before 2019-06-01 you must connect your computer to the USB port to get access via this address.

For controllers purchased after this date, the port labelled 192.168.7.2 or DEFAULT ETHERNET must be used. 

#### Features
- Configuration Free, Plug-&-Play
- Digital Communication with the MachineMotion Controller
- 4 x 24V Input Ports
- 4 x 24V Output Ports

### Technical Specifications

#### Input Ports
| Name                          | Specification                 | Units
|---                            |---                            |---    |
| Electrical Interface          | 10kohm pull-up resistor       | NA    |
| Voltage Range                 | 0 - 24                        | V     |
| Transition Voltage            | 9.025                         | V     |

#### Output Ports
| Name                          | Specification                 | Units
|---                            |---                            |---    |
| Electrical Interface          | Push-Pull Transistors         | NA    |
| High Voltage Range            | 23 - 24                       | V     |
| Low Voltage Range             | 0 - 1                         | V     |
| Sourcing Current Range        | 0 - 75                        | mA    |
| Sinking Current Range         | 0 - 100                       | mA    |

#### Pinout
The Digital IO Module contains 4 inputs and 4 outputs, each of which is grouped with a 24V and 0V supply connection for convenient wiring to external devices. The Digital IO Module is also equipped with 8 LED's to visualize the input and output signals. The LED's are located on the sides of the enclosure.

##### Input / Output
<p style="text-align:center;" ><img src="_media/digital_io_module_pinout_hq.png" width="60%" height="60%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 2: Digital IO Module Pinout.</em></p>


##### Input LED's
| Signal Type   | State         | Voltage (V)   | LED   |
|---            |---            |---            |---    |
| Input         | High          | 24            |ON     |
| Input         | Low           | 0             |OFF    |
| Input         | Floating      | 24            |ON     |

##### Output LED's
| Signal Type   | State         | Voltage (V)       | LED   |
|---            |---            |---            |---    |
| Output        | High          | 24            | ON |
| Output        | Low           | 0             | OFF   |

##### M12 Connector Pinout
| Pin Number    |Description        |
|---            |---                |
| 1             | 24V               |
| 2             | 0V                |
| 3             | RS485 A           |
| 4             | RS485 B           |
| 5             | Not Used          |
| 6             | Not Used          |
| 7             | Not Used          |
| 8             | shield / Earth    |


### Applications
The Digital IO Module can interface with external systems and devices that use 24V digital input/output control. The devices listed below are typical use cases:

- Programmable logic controllers (PLC's)
- Digital process sensors
- Relays
- Robot controllers
- Pneumatic actuators
- Push-buttons
- Lights and indicators

### Connecting to MachineMotion

The Digital IO Module can be connected to the MachineMotion controller via any one of the controller’s AUX ports (AUX1, AUX2, AUX3). See *Figure 3*.

<p style="text-align:center;" ><img src="_media/machine_motion_aux_connectors.png" width="60%" height="60%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 3: AUX ports on the MachineMotion controller.</em></p>

The MachineMotion controller will automatically detect the module and make it available. A maximum of three Digital IO Modules can be connected to a MachineMotion controller.

### Control
The Digital IO Module has a fixed factory address, which is indicated on its product information sticker. Ensure you use the correct address when communication with the module.

#### Vention ControlCenter

Use the [Jogger](http://192.168.7.2/_pendant/jogger.html) app to control the Digital IO Module outputs and visualize its input states.

You can access the ControlCenter software via your Chrome browser. Make sure your computer is connected to the controller via the 192.168.7.2 port (formerly labelled DEFAULT ETHERNET). Click on the Inputs / Outputs button (see *Figure 4*) to access the Digital IO Module control interface (*Figure 4*).

<p style="text-align:center;" ><img src="_media/control_center_io_control_edited.png" width="60%" height="60%"  <img style="border:1px solid grey;"> </p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 4: Accessing the Digital IO Module control interface.</em></p>

<p style="text-align:center;" ><img src="_media/control_center_digital_io_module.png" width="60%" height="60%"  <img style="border:1px solid grey;"> </p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 5: Digital IO Module control interface.</em></p>

#### MachineLogic
The [MachineLogic]() programming interface also allows for control of the Digital IO Module.

#### Python Programs
Refer to the latest [Python API](https://github.com/VentionCo/mm-python-api) for details on how to control the Digital IO Module with Python programs.