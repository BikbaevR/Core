import os

from core.core import Core
from config_files import MainConfig

class Initialization():

    @classmethod
    def run(cls):

        #Создание конфиг файлов
        MainConfig.create_main_config_file()
        Core.get_config_by_name('main').read_config()

        #Регистрация логгеров
        Core.create_logger(
            logger_name='main',
            logger_file_name='log',
            executable_file=__file__,
            path_to_log_file=Core.get_config_by_name('main').get('path_to_logger_files')
        )

        #Регистрация папок
        Core.register_folders(
            folder_name='csv',
            folder_path=os.path.join(Core.get_current_path(__file__), '_old_files'),
            custom_path=Core.get_config_by_name('main').get('path_to_csv_files'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )

        Core.register_folders(
            folder_name='used_csv',
            folder_path=os.path.join(Core.get_folder_by_name('csv'), 'done'),
            custom_path=Core.get_config_by_name('main').get('path_to_used_csv_files'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )

        Core.register_folders(
            folder_name='temp_files',
            folder_path=os.path.join(Core.get_current_path(__file__), 'temp_folder'),
            custom_path=Core.get_config_by_name('main').get('path_to_temp_files'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )

        Core.register_folders(
            folder_name='used_temp_folder',
            folder_path=os.path.join(Core.get_folder_by_name('temp_files'), 'done'),
            custom_path=Core.get_config_by_name('main').get('path_to_used_temp_files'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )

        Core.register_folders(
            folder_name='response',
            folder_path=os.path.join(Core.get_current_path(__file__), 'response'),
            custom_path=Core.get_config_by_name('main').get('path_to_response'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )
        Core.register_folders(
            folder_name='zips',
            folder_path=os.path.join(Core.get_current_path(__file__), 'zips'),
            custom_path=Core.get_config_by_name('main').get('path_to_save_archive'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )

        Core.register_folders(
            folder_name='path_to_logger_files',
            folder_path=os.path.join(Core.get_current_path(__file__), 'log'),
            custom_path=Core.get_config_by_name('main').get('path_to_logger_files'),
            enable_custom_path=Core.get_config_by_name('main').get('enable_custom_path')
        )

        #Создание/провека папок
        Core.check_or_create_folder(Core.get_folder_by_name('csv'), create_if_not_exist=True)
        Core.check_or_create_folder(Core.get_folder_by_name('used_csv'), create_if_not_exist=True)
        Core.check_or_create_folder(Core.get_folder_by_name('temp_files'), create_if_not_exist=True)
        Core.check_or_create_folder(Core.get_folder_by_name('used_temp_folder'), create_if_not_exist=True)
        Core.check_or_create_folder(Core.get_folder_by_name('response'), create_if_not_exist=True)
        Core.check_or_create_folder(Core.get_folder_by_name('zips'), create_if_not_exist=True)
        Core.check_or_create_folder(Core.get_folder_by_name('path_to_logger_files'), create_if_not_exist=True)

        #Конец
        Core.get_logger_by_name('main').info('Инициализация прошла успешно')