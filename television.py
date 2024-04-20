class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    
    def __init__(self)  -> None:
        """

        Initalize status for TV class with settings
        Sets TV off and on, mute, volume, channel, min and max values
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__volume_before_mute = self.__volume 

    def power(self) -> None:
        """

        Toggle power off and on, on it TRUE and off is FALSE
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """

        Toggle mute status, ONLY IF TV IS ON
        Mute should set volume to min and when unmute(mute = false) restores vlume status
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume_before_mute = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume_before_mute

    def channel_up(self) -> None:
        """

        Method used is add one to channel every time and when exceeds max channel goes in loop
        TV must be on for this method to work
        """
        if self.__status:
            nv = self.__channel + 1
            ww = nv % (Television.MAX_CHANNEL + 1)
            self.__channel = ww

    def channel_down(self) -> None:
        """

        Method used is negative one to channel, loops too if exceeds the min set value going back to max and backwards
        """
        if self.__status:
            pp = self.__channel - 1
            wr = pp % (Television.MAX_CHANNEL + 1)
            self.__channel = wr

    def volume_up(self) -> None:
        """

        Increases volume by one every time up to max, TV must be on for this method to work
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_before_mute
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """

        Decreases volume by one everytime up to min value, TV must be on for this to work
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_before_mute
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """
        Method that returns a string representing the TV status, channel, volume
        Good for logging state of TV(Research purposes)
        """
        if self.__status:
            ps = 'True'
        else:
            ps = 'False'
        cs = self.__channel
        vs = self.__volume
        rs = f"Power = {ps}, Channel = {cs}, Volume = {vs}"
        return rs
