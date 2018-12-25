sudo python3 "/home/pi/a/thermostat/main.py" \
--mqtt_server_ip "192.168.2.52" \
--mqtt_server_port "1883" \
--mqtt_topic_set_temperature "thermostat/set_temperature" \
--mqtt_topic_ack_temperature "thermostat/ack_temperature" \
--thermostat_pin_a "16" \
--thermostat_pin_b "18" \
--thermostat_delay "0.03" \
