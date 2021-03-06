class Television:
    """
    A class representing details for a television object.
    """
    MIN_CHANNEL: int = 0     # Minimum TV channel
    MAX_CHANNEL: int = 3     # Maximum TV channel

    MIN_VOLUME: int = 0      # Minimum TV volume
    MAX_VOLUME: int = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Function to initialize the television's properties __channel, __volume, and __status.
        """
        self.__channel: int = Television.MIN_CHANNEL   # Set __channel to MIN_CHANNEL by default 
        self.__volume: int = Television.MIN_VOLUME     # Set __volume to MIN_VOLUME by default
        self.__status: bool = False                    # Set __status False by default, "off".


    def power(self) -> None:
        """
        Function to change the property __status of the television alternating between True and False with each run.
        """
        self.__status = not self.__status

    def channel_up(self) -> None:
        """
        Function to increment the television's property __channel up by one and to roll over back to MIN_CHANNEL when above MAX_CHANNEL
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Function to increment the television's property __channel down by one and to roll over back to MAX_CHANNEL when below MIN_CHANNEL
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Function to increment the television's property __volume up by one and to stop when it reaches MAX_VOLUME
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Function to increment the television's property __volume down by one ant to stop when it reaches MIN_VOLUME
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Function that modifies what Television returns when its outputed as a string.
        :return: The string that is formated to contain the properties __status, __channel, __volume.
        """
        return "TV status: Is on = {}, Channel = {}, Volume = {}".format(self.__status, self.__channel, self.__volume)
        
