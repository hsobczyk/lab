import pytest
from classes import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"