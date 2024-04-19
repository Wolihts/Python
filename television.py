class Television:
    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False  # TV is initially off
        self.__muted = False   # TV is initially unmuted
        self.__volume = Television.MIN_VOLUME  # Start at minimum volume
        self.__channel = Television.MIN_CHANNEL  # Start at minimum channel

    def power(self):
        # Toggle the TV's power status
        self.__status = not self.__status

    def mute(self):
        if self.__status:  # Can only mute or unmute if TV is on
            self.__muted = not self.__muted
            if not self.__muted:
                # If TV is unmuted, reset volume (as per the provided note)
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        if self.__status:  # Can only change channel if TV is on
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:  # Can only change channel if TV is on
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status and not self.__muted:  # Can only change volume if TV is on and not muted
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status and not self.__muted:  # Can only change volume if TV is on and not muted
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f"Power = {'On' if self.__status else 'Off'}, Channel = {self.__channel}, Volume = {self.__volume}"
