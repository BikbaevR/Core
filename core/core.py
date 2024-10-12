import os
from typing import List, Any

from .AnswerClass import Answer
from .config import Config


class Core:

    __config_list: dict = {}

    @classmethod
    def check_or_create_folder(cls, folder_path: str, create_if_not_exist=False) -> Answer:
        answer = Answer()

        if len(folder_path) <= 0:
            answer.set_status(False)
            answer.set_message('Аргумент [folder_path] не передан')
            return answer

        try:
            folder_is_exist = os.path.exists(folder_path)
        except Exception as e:
            answer.set_error(True)
            answer.set_status(False)
            answer.set_message(f'Не удалось проверить папку по пути [{folder_path}]')
            answer.set_system_error(e)
            return answer

        if folder_is_exist:
            answer.set_status(True)
            answer.set_error(False)
            answer.set_message(f'Папка по пути [{folder_path}] существует')
            return answer

        elif not folder_is_exist and create_if_not_exist:
            try:
                os.makedirs(folder_path)
                answer.set_status(True)
                answer.set_error(False)
                answer.set_message(f'Папка по пути [{folder_path}] успешно создана')
                return answer
            except Exception as e:
                answer.set_error(True)
                answer.set_status(False)
                answer.set_message(f'Не удалось создать папку по пути [{folder_path}]')
                answer.set_system_error(e)
                return answer

        else:
            answer.set_status(False)
            answer.set_error(False)
            answer.set_message(f'Папка по пути [{folder_path}] не существует')
            return answer


    @classmethod
    def create_config_file(cls, config_name: str, config_file_name: str, config_fields: dict) -> Answer:
        answer = Answer()

        if len(config_name) <= 0:
            answer.set_status(False)
            answer.set_error(True)
            answer.set_message(f'Параметр [{config_name}] не может быть пустым')
            return answer

        if len(config_file_name) <= 0:
            answer.set_status(False)
            answer.set_error(True)
            answer.set_message(f'Параметр [{config_file_name}] не может быть пустым')
            return answer

        if len(config_file_name) <= 0:
            answer.set_status(False)
            answer.set_error(True)
            answer.set_message(f'Параметр [{config_fields}] не может быть пустым')
            return answer

        cls.__config_list[config_name] = Config(config_file=config_file_name, default_config=config_fields)
        answer.set_status(True)
        answer.set_error(False)
        answer.set_message(f'Конфигурационный файл [{config_name}] успешно создан')
        return answer

    @classmethod
    def get_config_by_name(cls, config_name: str) -> list[Answer | Config]:
        answer = Answer()

        if len(config_name) <= 0:
            answer.set_status(True)
            answer.set_error(True)
            answer.set_message(f'Параметр [{config_name}] не может быть пустым')
            return [answer, None]

        try:
            config = cls.__config_list[config_name]
            answer.set_status(True)
            answer.set_error(False)
            answer.set_message(f'Конфигурационный файл с названием [{config_name}] найден')
            return [answer, config]

        except Exception as e:
            answer.set_status(False)
            answer.set_error(True)
            answer.set_message(f'Конфигурационный файл с названием [{config_name}] не найден')
            answer.set_system_error(e)
            return [answer, None]