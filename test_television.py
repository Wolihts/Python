
import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_initial_status_channel_volume(tv):
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_power_on(tv):
    tv.power()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_power_off(tv):
    tv.power()
    tv.power()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_mute_when_tv_on_and_volume_up_once(tv):
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_unmute_when_tv_on(tv):
    tv.power()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_mute_when_tv_off(tv):
    tv.mute()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_unmute_when_tv_off(tv):
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_channel_up_when_tv_off(tv):
    tv.channel_up()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_channel_up_when_tv_on(tv):
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = On, Channel = 1, Volume = 0"

def test_channel_up_past_max(tv):
    tv.power()
    for _ in range(Television.MAX_CHANNEL + 1):
        tv.channel_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_channel_down_when_tv_off(tv):
    tv.channel_down()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_channel_down_past_min(tv):
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = On, Channel = 3, Volume = 0"

def test_volume_up_when_tv_off(tv):
    tv.volume_up()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_volume_up_when_tv_on(tv):
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 1"

def test_volume_up_when_muted(tv):
    tv.power()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_volume_up_past_max(tv):
    tv.power()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 2"

def test_volume_down_when_tv_off(tv):
    tv.volume_down()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"

def test_volume_down_when_tv_on(tv):
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_volume_down_when_muted(tv):
    tv.power()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"

def test_volume_down_past_min(tv):
    tv.power()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_up()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_down()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"
