import pytest
from classes import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    def test_power(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    def test_volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"

        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
