import pytest
from television import *

class TestTelevision:
    @pytest.fixture
    def tv(self):
        return Television()

    def testchannel_volume(self, tv):
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def testpower_on_off(self, tv):
        tv.power()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"
        tv.power()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def testmute_unmute(self, tv):
        tv.power()
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def testchannel_up_down(self, tv):
        tv.power()
        tv.channel_up()
        assert str(tv) == "Power = True, Channel = 1, Volume = 0"
        tv.channel_up()
        assert str(tv) == "Power = True, Channel = 2, Volume = 0"
        tv.channel_down()
        assert str(tv) == "Power = True, Channel = 1, Volume = 0"
        tv.channel_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def testvolume_up_down(self, tv):
        tv.power()
        tv.volume_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def testmutevolume_controls(self, tv):
        tv.power()
        tv.mute()
        tv.volume_up()
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"
        tv.mute()
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

