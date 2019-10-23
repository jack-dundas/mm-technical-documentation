# Vention Linear Axis Setup
This *How-to-Guide* covers the setup of motors and sensors on a Vention Linear axis.

## Background

Vention linear axes equipped with the MachineMotion controller provide a true motion control platform. This allows precise & accurate motion to be performed.

For motion control to be possible, a position reference must exist. This is what homing refers to, the action of finding the position reference of an axis. This position reference is also called *home* or *zero*.

End-stop sensors are used to perform homing operations. In order for the homing to be properly done, end-stop sensors must be placed in the appropriate location and connected to the right port on the MachineMotion controller. Installation of end-stop sensors also depends on how the motor is installed on the linear axis.

## Motors

### Rotation Direction
By convention, the motors have a positive and a negative rotation direction. This is an important consideration when installing the motor on a linear axis. When sending motion commands to the controller (for example a relative move of +200mm), it is important that the axis moves in the desired direction.

The rotation direction convention is shown in *Figure 1* and *Figure 2*:

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/881/large/positive_motor_direction.png?1548034463" width="25%" height="25%"></p>

***Figure 1: Motor Positive Rotation Direction (Front Shaft Perspective)***


<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/882/large/negative_motor_direction.png?1548034476" width="25%" height="25%"></p>

***Figure 2: Motor Negative Rotation Direction (Front Shaft Perspective)***


### Linear Axis Direction
In order to satisfy the application requirements, positive rotation of the motor shaft should result in linear motion in the desired direction. *Figures 3 to 6* show how the linear axis move depending on where the motor is installed.

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/885/large/positive_axis_direction_quadrant_3.png?1548034507" width="60%" height="60%"></p>

***Figure 3: Motor Placement #1***

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/884/large/positive_axis_direction_quadrant_2.png?1548034505" width="60%" height="60%"></p>

***Figure 4: Motor Placement #2***

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/883/large/positive_axis_direction_quadrant_1.png?1548034504" width="60%" height="60%"></p>

***Figure 5: Motor Placement #3***

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/886/large/positive_axis_direction_quadrant_4.png?1548034508" width="60%" height="60%"></p>

***Figure 6: Motor Placement #4***

## End-Stop sensors
Linear axes require the use of end-stop sensors, for two main reasons:
- Perform homing operations (placing the axis in a known position, called home or zero)
- Disable motion in the event of an over or under travel event.

Inductive sensors are the preffered option for end-stop sensing since they are non-contact and less subject to environmental interference.

- M18 Inductive Proximity Sensor (Sn = 10 mm): [CE-SN-004-0001](https://www.vention.io/parts/244)


### Connections

#### Home Sensor (also called under-travel sensor)
The home sensor should be connected to the SENSORxA on the MachineMotion controller. For axis 1, the home sensor should be connected to SENSOR1A, for axis 2 SENSOR2A and for axis 3 SENSOR3A.

#### Over-Travel Sensor
The over-travel sensor should be connected to the SENSORxB on the MachineMotion controller. For axis 1, the home sensor should be connected to SENSOR1B, for axis 2 SENSOR2B and for axis 3 SENSOR3B.

### Position

#### Home / Under-Travel Sensor
When moving the axis in the negative direction, the gantry should be moving towards SENSOR1A (home / under-travel sensor).

#### Over-Travel Sensor
When moving the axis in the positive direction, the gantry should be moving towards SENSOR1B (over-travel sensor).

The image below details how to connect and position the end-stop sensors for a specific motor position. Important points:

- The *home* sensor is positioned such that a negative motion moves towards it
- The *home* sensor is connected to port SENSOR1A 
- The *over-travel* sensor is positioned such that a positive motion moves towards it
- The *over-travel* sensor is connected to port SENSOR1B

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/888/large/sensor_connection_example.png?1548034531" width="60%" height="60%"></p>

***Figure 7: End-stop Connections Example for a Specific Motor Connection***

## Direction Reversal

It is posible that for design reasons, the motor has to be placed at a specific place on the linear axis (due to space or mechnical constraints). This could result in an undesired positive motion direction of the linear axis. For this reason, there is a also a software command that permits reversing the direction of a given axis. The basic Vention Apps offer this feature:

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/887/large/control_center_reverse_axis.png?1548034530" width="50%" height="50%"></p>

***Figure 8: Basic 1-Axis Linear Motion App showing the location of the reverse axis feature***

**++This configuration reverses the motor default rotation direction, but also reverses the position of the home and over-travel sensors.++**

Going back to the example of *Figure 7*, reversing the axis results in the following configuration.

- The *home* sensor is positioned such that a negative motion moves towards it
- The *home* sensor is connected to port SENSOR1B 
- The *over-travel* sensor is positioned such that a positive motion moves towards it
- The *over-travel* sensor is connected to port SENSOR1A

<p style="text-align:center;" ><img src="https://s3.amazonaws.com/ventioncms/vention_images/images/000/000/889/large/sensor_connection_example_reverse_direction.png?1548034533" width="60%" height="60%"></p>

***Figure 9: End-stop Connections Example for a Specific Motor Connection using software axis reversal***