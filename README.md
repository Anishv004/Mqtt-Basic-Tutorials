Before getting into the code, make sure that you have installed Mosquitto eclipse in your local machine.

First, run the mqtt_subscriber.py in a command line, and then run the mqtt_publish1.py in a different command line instance. This is just to show that the different command lines can be replaced by different machines, and the messages can be transferred through mqtt server. On running so, we would be able to see the messages published by mqtt_publish1.py in the output terminal of mqtt_subscriber.py. 

The status of all the publish and subscribe requests can be monitored by running the server status using the following command.
mosquitto -v -c test.conf