class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__volume_before_mute = self.__volume 

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume_before_mute = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume_before_mute

    def channel_up(self):
        if self.__status:
            nv = self.__channel + 1
            ww = nv % (Television.MAX_CHANNEL + 1)
            self.__channel = ww

    def channel_down(self):
        if self.__status:
            pp = self.__channel - 1
            wr = pp % (Television.MAX_CHANNEL + 1)
            self.__channel = wr

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_before_mute
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_before_mute
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self):
        if self.__status:
            ps = 'True'
        else:
            ps = 'False'
        cs = self.__channel
        vs = self.__volume
        rs = f"Power = {ps}, Channel = {cs}, Volume = {vs}"
        return rs


