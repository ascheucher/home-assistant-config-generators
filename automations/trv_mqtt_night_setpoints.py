night_values = [("trv.gf_kitchen", 19),
                ("trv.gf_guest-room", 18),
                ("trv.gf_hw_east", 18),
                ("trv.gf_hw_west", 19),
                ("trv.gf_bath", 18),
                ("trv.gf_toilet", 15),
                ("trv.uf_bedroom", 22),
                ("trv.uf_living-room_west", 21),
                ("trv.uf_living-room_north", 21),
                ("trv.uf_office", 19)]

for night_value in night_values:
    print(f"""  - service: mqtt.publish
    data:
      topic: zigbee2mqtt/{night_value[0]}/set
      payload: '{{"occupied_heating_setpoint": {night_value[1]} }}'
      retain: true""")

