import os

from core.core import Core

Core.set_folder('csv', Core.get_config_by_name('main').get('path_to_csv_files') or os.path.join(Core.get_current_path(), '_old_files'))