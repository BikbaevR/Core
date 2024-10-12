from core.core import Core

# answer = Core.check_or_create_folder(r'C:\Users\workPc\Desktop\New folder (3)', create_if_not_exist=True)
#
# print(answer.get_status())
# print(answer.get_error())
# print(answer.get_messages())

answer = Core.create_config_file('test', 'test.conf', {'test': False})
# print(answer.get_status())
# print(answer.get_error())
# print(answer.get_messages())

answer, config = Core.get_config_by_name('test')
# print(answer.get_status())
# print(answer.get_error())
# print(answer.get_messages())

conf = config.read_config()
print(conf.get('test'))

# print(type(conf))
# print(conf.get('test'))

