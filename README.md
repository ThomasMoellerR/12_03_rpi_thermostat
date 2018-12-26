#  MQTT_Thermostat

## Follow the next steps to control your thermostat with a raspberry pi

## For hardware connection see:
https://www.youtube.com/watch?v=WzFFA5_GKVo

## Create a ssh connection to your pi
    ssh pi@192.168.x.x

## Step 1: Download these two repositories into your home directory
    git clone https://github.com/ThomasMoellerR/MQTT_Thermostat.git
    git clone https://github.com/eclipse/paho.mqtt.python

## Step 2: Install MQTT module for python3
    cd paho.mqtt.python
    sudo python3 setup.py install
    cd ..
    sudo rm -r paho.mqtt.python

## Step 3: Install tmux
    sudo apt-get install tmux


## Step 4: Install a new crontab
    crontab -e

`@reboot /bin/bash /home/pi/MQTT_Thermostat/tmux.sh`

## Step 5: Make "/home/pi/MQTT_Thermostat/tmux.sh" executable
    sudo chmod +x /home/pi/MQTT_Thermostat/tmux.sh

## Step 6: Configure MQTT client (thermostat)
    nano /home/pi/MQTT_Thermostat/main.sh

`--mqtt_server_ip "192.168.2.52" \`

`--mqtt_server_port "1883"`

`--mqtt_topic_set_temperature "thermostat/set_temperature" \`

`--mqtt_topic_ack_temperature "thermostat/ack_temperature" \`


## Step 7: Reboot your Pi or start the tmux session manually
    sudo reboot

    or

    bash /home/pi/MQTT_Thermostat/tmux.sh

## Finish: When you arrive at this point, you are done


## Troubleshooting:


###  A: Set the Termostat to the operating state "manu"

###  B: Turn the encoder one step to the right


###  C: Check if the programm is running

with the command "tmux a" you can attach to a running session

    tmux a

with the command "ctrl+b" inside the session with a "d" followed you can detach from this session and the programm keeps running

    ctrl+b

    d
