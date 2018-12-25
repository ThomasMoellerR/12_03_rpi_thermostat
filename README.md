#  MQTT_Thermostat
## Step 1: Download these two repositories into your home directory /home/pi"
    git clone https://github.com/ThomasMoellerR/MQTT_Thermostat.git
    git clone https://github.com/eclipse/paho.mqtt.python

## Step 2: Install MQTT module for python3
    cd paho.mqtt.python
    python3 setup.py install
    cd ..

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


## Step 6: Reboot your Pi
    sudo reboot
