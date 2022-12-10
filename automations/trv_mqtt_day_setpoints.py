day_values = [("trv.gf_kitchen", 20),
              ("trv.gf_guest-room", 19),
              ("trv.gf_hw_east", 21),
              ("trv.gf_hw_west", 23),
              ("trv.gf_bath", 20),
              ("trv.gf_toilet", 18),
              ("trv.uf_bedroom", 20),
              ("trv.uf_living-room_west", 22),
              ("trv.uf_living-room_north", 22),
              ("trv.uf_office", 23)]

for night_value in day_values:
    print(f"""  - service: mqtt.publish
    data:
      topic: zigbee2mqtt/{night_value[0]}/set
      payload: '{{"occupied_heating_setpoint": {night_value[1]} }}'
      retain: true""")
