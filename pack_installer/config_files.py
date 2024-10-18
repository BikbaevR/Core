from core.core import Core

class MainConfig:

    @classmethod
    def create_main_config_file(cls):
        Core.create_config_file(
            config_name='main',
            config_file_name='main_config.cfg',
            config_fields={
                'ip_port': '',
                'time_to_check_main_colder': '',
                'personal_mode': False,
                'enable_custom_path': False,
                'path_to_csv_files': '',
                'path_to_used_csv_files': '',
                'path_to_temp_files': '',
                'path_to_used_temp_files': '',
                'path_to_response': '',
                'path_to_save_archive': '',
                'path_to_logger_files': '',
                'auto_push': False,
                'pause_to_push':'',
                'change_date_in_pp': False,
                'date_to_pp':'',
                'pp_sign':'',
                'request_timeout':'',
                'csv_from_git': False,
                'pause_between_get_csv': 3600,
                'link_to_csv_repo': '',
                'path_to_save_git_data': '',
                'app_black_list': '',
                'remove_status_hld_from_tsa': False,
                'division_into_folders': False,
                'deleting_deleted_data': False
            }
        )
