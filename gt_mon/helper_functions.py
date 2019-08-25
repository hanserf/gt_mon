import json


class ImportConfig(object):
    def __init__(self, config):
        self.__dict__ = json.load(config)


class ResultStructure:
    def __init__(self, temp_indoor, temp_outdoor, timestamp, pwm_white_led, pwm_purple_led, power_consumption ):
        self.temp_indoor = temp_indoor
        self.temp_outdoor = temp_outdoor
        self.timestamp=timestamp
        self.pwm_white_led=pwm_white_led
        self.pwm_purple_led=pwm_purple_led
        self.power_consumption=power_consumption
