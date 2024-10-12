import os
import sys

class Config:
    def __init__(self, config_file="config.cfg", directory=None, default_config=None):
        self.config_file = config_file
        self.config_directory = directory if directory is not None else os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        if default_config is None:
            self.default_config = {
                "default": "default config",
            }
        else:
            self.default_config = default_config
        
        self.config = self.default_config.copy()

        if not os.path.exists(self.config_file):
            self.create_default_config()

    def create_default_config(self):
        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                for key, value in self.default_config.items():
                    file.write(f"{key} = {value}\n")
        except Exception as e:
            print(f"Ошибка при создании файла конфигурации: {e}")

    def read_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    if '=' in line:
                        key, value = line.split('=', 1)
                    elif ':' in line:
                        key, value = line.split(':', 1)
                    else:
                        continue 
                    
                    key = key.strip()
                    value = value.strip().replace("'", '')
                    value = value.replace('"', '')

                    if key in self.config:
                        if value.lower() == 'true':
                            value = True
                        elif value.lower() == 'false':
                            value = False
                        elif value.lower() == 'None':
                            value = None
                        elif value.lower() == '':
                            value = None
                        elif value.isdigit():
                            value = int(value)

                        self.config[key] = value
                    else:
                        print(f"Неизвестный параметр: {key}")

        except FileNotFoundError:
            print(f"Файл {self.config_file} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def get(self, key):
        return self.config.get(key)
