import json
import datetime as dt
import time as time

class ImportConfig(object):
    def __init__(self, config):
        self.__dict__ = json.load(config)


class ResultStructure:
    def __init__(self,sensor_ids, light_states,temp_indoor, temp_outdoor, pwm_white_led, pwm_purple_led, power_consumption ):

        self.temp[0] = temp_indoor
        self.temp[1] = temp_outdoor
        self.unixtime = time.time()
        self.datetime = dt.datetime.datetime.utcfromtimestamp(self.unixtime).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.ds18b20_id[0] = sensor_ids[0]
        self.ds18b20_id[1] = sensor_ids[0]
        self.light_states[0] = light_states[0]
        self.light_states[1] = light_states[1]
        self.pwm_value[1] = float(100 * (pwm_purple_led/255))
        self.pwm_value[0] = float(100 * (pwm_white_led /255))
        self.power_consumption=power_consumption
