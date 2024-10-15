import threading
import time
import os
import sys

from datetime import datetime
from .config import Config

class Logger:
    def __init__(self, filename=None, executable_file=None, path_to_log_file: str = None):
        self._date = datetime.now().strftime('%d_%m_%Y')
        self._filename = filename + '_' + self._date + '.log' if filename is not None else 'log_' + self._date + '.log'

        if path_to_log_file:
            self._directory = f'{path_to_log_file}'
        else:
            self._directory = os.path.join(
                os.path.dirname(sys.executable), 'log'
            ) if getattr(sys, 'frozen',False) else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log')

        self._executable_file = executable_file
        self._additional_file_for_errors_name = 'all_errors_' + self._date + '.log'

        self._lock = threading.Lock()

        self._create_directory_if_not_exists(self._directory)

        self.__config = Config(config_file='logger.cfg', default_config={
            'logger_enable': True,
            'info_enable': True,
            'debug_enable': False,
            'error_enable': True,
            'warning_enable': True,
            'additional_file_for_errors': True
        })

        self.__config.read_config()
        self._logger_enable = self.__config.get("logger_enable")
        self._info_enable = self.__config.get("info_enable")
        self._debug_enable = self.__config.get("debug_enable")
        self._error_enable = self.__config.get("error_enable")
        self._warning_enable = self.__config.get("warning_enable")
        self._additional_file_for_errors = self.__config.get("additional_file_for_errors")

    @staticmethod
    def _create_directory_if_not_exists(dir_path: str):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def _add_empty(log_type) -> str:
        if log_type == 'INFO':
            return ' ' * 3
        if log_type != 'WARNING':
            return ' ' * 2
        else:
            return ''

    def _log(self, level, message, to_console, to_file):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        if self._debug_enable and self._executable_file:
            formatted_message = f'[{level}] {self._add_empty(level)} {timestamp} [{self._executable_file}] - {message}\n'
        else:
            formatted_message = f'[{level}] {self._add_empty(level)} {timestamp} - {message}\n'

        if self._logger_enable:
            with self._lock:
                if to_console:
                    print(f'[{level}] {self._add_empty(level)} {timestamp} - {message}')
                if to_file:
                    with open(os.path.join(self._directory, self._filename), 'a', encoding='utf-8') as f:
                        f.write(formatted_message)

                if self._additional_file_for_errors and level.lower() == 'error':
                    with open(os.path.join(self._directory, self._additional_file_for_errors_name), 'a', encoding='utf-8') as f:
                        f.write(f'[{level}] {self._add_empty(level)} {timestamp} [{self._executable_file}] - {message}\n')

    def info(self, message, to_console=True, to_file=True):
        if self._info_enable:
            self._log("INFO", message, to_console, to_file)

    def debug(self, message, to_console=True, to_file=True):
        if self._debug_enable:
            self._log("DEBUG", message, to_console, to_file)

    def error(self, message, to_console=True, to_file=True):
        if self._error_enable:
            self._log("ERROR", message, to_console, to_file)

    def warning(self, message, to_console=True, to_file=True):
        if self._warning_enable:
            self._log("WARNING", message, to_console, to_file)

    def line(self, to_console=True, to_file=True):
        if self._info_enable and self._debug_enable:
            # self._log("INFO", '-' * 20, to_console, to_file)
            ...
    def config(self, message):
        self._log("CONF", message, to_console=False, to_file=True)