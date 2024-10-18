import os
import sys

from .config import Config
from .logger import Logger


class Core:

    __logger_list: dict[str, Logger] = {}
    __config_list: dict[str, Config] = {}
    __folder_list: dict[str, str] = {}


    @classmethod
    def __check_argument(cls, argument: str or dict) -> bool:
        if len(argument) == 0:
            return True
        return False

    @classmethod
    def check_or_create_folder(cls, folder_path: str, create_if_not_exist: bool = False) -> None:

        if cls.__check_argument(folder_path):
            raise Exception("Аргумент [folder_path] не передан")

        try:
            folder_is_exist = os.path.exists(folder_path)
        except:
            raise Exception(f'Не удалось проверить папку по пути [{folder_path}]')


        if not folder_is_exist and create_if_not_exist:
            try:
                os.makedirs(folder_path)
            except:
                raise Exception(f'Не удалось создать папку по пути [{folder_path}]')
        if folder_is_exist:
            ...
        else:
            raise Exception(f'Папка по пути [{folder_path}] не существует')


    @classmethod
    def create_config_file(cls, config_name: str, config_file_name: str, config_fields: dict):

        if cls.__check_argument(config_name):
            raise Exception(f'Параметр [config_name] не может быть пустым')

        if cls.__check_argument(config_file_name):
            raise Exception(f'Параметр [config_file_name] не может быть пустым')

        if cls.__check_argument(config_fields):
            raise Exception(f'Параметр [config_fields] не может быть пустым')

        if config_name in cls.__config_list:
            raise Exception(f'Конфигурационный файл с именем [{config_name}] уже существует')

        try:
            cls.__config_list[config_name] = Config(
                config_file=config_file_name,
                default_config=config_fields
            )
        except Exception as e:
            raise Exception(f'Не удалось создать конфигурацию - {e}')


    @classmethod
    def get_config_by_name(cls, config_name: str):

        if cls.__check_argument(config_name):
            raise Exception(f'Параметр [config_name] не может быть пустым')

        try:
            return cls.__config_list[config_name]
        except:
            raise Exception(f'Конфигурационный файл с названием [{config_name}] не найден')


    @classmethod
    def create_logger(cls, logger_name: str, logger_file_name: str, executable_file: str = None, path_to_log_file: str = None):
        if cls.__check_argument(logger_name):
            raise Exception(f'Параметр [logger_name] не может быть пустым')

        if logger_name in cls.__logger_list:
            raise Exception(f'Лог файл с именем [{logger_name}] уже существует')

        try:
            cls.__logger_list[logger_name] = Logger(
                filename=logger_file_name,
                executable_file=executable_file,
                path_to_log_file=path_to_log_file
            )
        except:
            raise Exception(f'Не удалось создать объект логгера - [{logger_name}]')


    @classmethod
    def get_logger_by_name(cls, logger_name: str):
        if cls.__check_argument(logger_name):
            raise Exception(f'Параметр [logger_name] не может быть пустым')

        try:
            return cls.__logger_list[logger_name]
        except:
            raise Exception(f'Логгер с названием [{logger_name}] не найден')

    @classmethod
    def get_files_by_extension(cls, folder_path: str, extension: str = None, nested_folders: bool = False):

        _files: list[str] = []

        if not os.path.exists(folder_path):
            raise Exception(f'Не удалось найти путь [{folder_path}]')

        if nested_folders:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if extension is not None:
                        if file.endswith(extension):
                            _files.append(os.path.join(root, file))
                    else:
                        _files.append(os.path.join(root, file))
        else:
            for file in os.listdir(folder_path):
                if extension is not None:
                    if file.endswith(extension):
                        _files.append(os.path.join(folder_path, file))
                else:
                    _files.append(os.path.join(folder_path, file))

        return _files

    @classmethod
    def get_current_path(cls, file):
        return os.path.dirname(os.path.dirname(sys.executable)) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.dirname(os.path.abspath(file)))

    @classmethod
    def register_folders(cls, folder_name: str, folder_path: str = None, custom_path: str = None, enable_custom_path: bool = False):
        if len(folder_path) <= 0:
            raise Exception(f'Параметр [folder_path] не может быть пустым')

        if folder_path in cls.__folder_list:
            raise Exception(f'Папка [{folder_path}] уже зарегистрирована')

        if enable_custom_path and custom_path is not None:
            cls.__folder_list[folder_name] = custom_path
        else:
            cls.__folder_list[folder_name] = folder_path

    @classmethod
    def get_folder_by_name(cls, folder_name: str):
        if len(folder_name) <= 0:
            raise Exception(f'Параметр [folder_path] не может быть пустым')

        try:
            return cls.__folder_list[folder_name]
        except:
            raise Exception(f'Папка с именем [{folder_name}] не найдена')
