
class Answer:
    def __init__(self):
        self.__status: bool = False
        self.__error: bool = False
        self.__messages: list = []
        self.__system_error: str = ''

    def set_status(self, status: bool) -> None:
        self.__status = status

    def set_error(self, error: bool) -> None:
        self.__error = self.__error

    def set_message(self, message: any) -> None:
        self.__messages.append(str(message))

    def set_system_error(self, error: any) -> None:
        self.__system_error = str(error)

    def get_error(self) -> bool:
        return self.__error

    def get_status(self) -> bool:
        return self.__status

    def get_messages(self) -> list:
        return self.__messages

    def get_system_error(self) -> str:
        return self.__system_error

