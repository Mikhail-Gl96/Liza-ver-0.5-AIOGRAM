# import os
#
# from config import _COMMANDS_DIR, _base_root
#
# if __name__ == "__main__":
#     _base_root = os.getcwd().split(f"{_COMMANDS_DIR}")[0]
#
# path_handler_dir = _base_root + f"{_COMMANDS_DIR}"
# handler_dir = os.listdir(path_handler_dir)
# handler_dir_files = [i for i in handler_dir if not os.path.isdir(path_handler_dir + f'\\{i}')]
# handler_dir_dirs = [i for i in handler_dir if os.path.isdir(path_handler_dir + f'\\{i}')]
#
# # print(f'\n\n\n'
# #       f'path_handler_dir= {path_handler_dir}\n'
# #       f'handler_dir= {handler_dir}\n'
# #       f'handler_dir_files= {handler_dir_files}\n'
# #       f'handler_dir_dirs= {handler_dir_dirs}')
#
#
# def get_files_paths(path):
#     temp_paths = list()
#     for i in os.listdir(path):
#         # print(f'    inside func object= {i},  path= {path}')
#         if os.path.isdir(path + f'\\{i}'):
#             if os.path.isdir(path + f'\\{i}'):
#                 # print(f'        {i} is a dir')
#                 temp_paths.extend(get_files_paths(path + f'\\{i}'))
#
#         else:
#             # print(f'        {i} is a file')
#             temp_paths.append(path + f'\\{i}')
#     # print(f'temp_paths ===== {temp_paths}')
#     return temp_paths.copy()
#
#
# def get_commands_from_file(file_path):
#     BOT_COMMANDS = dict()
#     with open(f'{file_path}', 'r', encoding='utf-8') as file_handlers:
#         flag_find_command = False
#         local_list = [None, None]
#         for i in file_handlers:
#             if i.startswith('# command'):
#                 flag_find_command = True
#                 continue
#             if flag_find_command is True:
#                 if i.startswith('# '):
#                     local_list[1] = i.split("# ")[1]
#                 elif i.startswith('@dp.message_handler(commands=['):
#                     local_list[0] = i[i.find("[") + 1:i.find(']')]
#                     local_dict = {
#                         local_list[0].replace("'", ""): local_list[1].replace('\n', ''),
#                     }
#                     BOT_COMMANDS.update(local_dict.copy())
#                     local_list = [None, None]
#                     flag_find_command = False
#                 else:
#                     flag_find_command = False
#     return BOT_COMMANDS
#
#
# # new_str = '\n'
# # print(f'\n\n\n'
# #       f'get_dirs_paths = {f"{new_str}".join(get_files_paths(path_handler_dir))}')
#
#
# def get_all_commands(path):
#     BOT_COMMANDS = dict()
#     for file_path in get_files_paths(path):
#         BOT_COMMANDS.update(get_commands_from_file(file_path))
#     return BOT_COMMANDS
#
#
# BOT_COMMANDS = get_all_commands(path_handler_dir)
#
#
# # commands_as_a_list = [f'Команда: /{i} - {BOT_COMMANDS.get(i)}' for i in BOT_COMMANDS.keys()]
# # print('\n'.join(commands_as_a_list))
